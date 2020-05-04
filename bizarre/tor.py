from subprocess import getoutput
from time import sleep

import http.cookiejar
import mechanize
import socks
import socket
import random

class Tor():

    def __init__(self):
        self.alive = True

    def install_tor(self):
        pass

    def restart_tor(self, num = 3):
        getoutput("service tor restart")
        sleep(1.5)
        self.update_identity(num)

    def stop_tor(self):
        getoutput("service tor stop")
        print('Tor stopped')

    def create_browser(self):
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(False)
        br.set_cookiejar(http.cookiejar.LWPCookieJar())
        br.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24')]
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        return br

    def get_ip(self):
        try:
            ip = None
            br = self.create_browser()
            ip = br.open('https://api.ipify.org/?format=text', timeout=1.5).read()
            br.close()
        except Exception as e:
            pass
        finally:
            if not self.alive:
                self.exit()
            return ip

    def update_identity(self, recur=3):
        socks.socket.setdefaulttimeout(5)
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
        socket.socket = socks.socksocket

        try:
            ip = self.get_ip()
            if all([not ip, recur]):
                print('Error: Network unreachable')
                reset_counts = 2
                for _ in range(30):
                    if not self.alive:
                        return
                    ip = self.get_ip()
                    if ip:
                        break
                    else:
                        if reset_counts:
                            reset_counts -= 1
                            getoutput('service network-manager restart')
                        sleep(1)
                if not ip:
                    self.restart_tor(recur-1)
            self.ip = ip
            print('Ip is', self.ip)
        except Exception as e:
            print(e)
