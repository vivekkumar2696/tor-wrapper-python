from .utils import Utils

from subprocess import getoutput
from time import sleep

import http.cookiejar
import mechanize
import socks
import socket
import random

"""
    Class use to handle all the tor operations including restarting, stoping, creating browsers, updating identity

    Could be used as a base class for extending functionalities
"""
class Tor():

    def __init__(self):
        self.alive = True

    def install_tor(self):
        # TODO: Add install functionality for different operating systems
        pass

    """
        Restart tor service
        Parameters:
        pwd: Pwd of linux shell
        num: Used as a threshold for retrying in case of errors
    """
    def restart_tor(self, pwd = None, num = 3):
        Utils.call_shell_command("service tor restart", pwd)
        sleep(1.5)
        self.update_identity(num, pwd)

    """
        Stop tor service
    """
    def stop_tor(self, pwd = None):
        Utils.call_shell_command("service tor stop", pwd)
        print('Tor stopped')

    """
        Create a browser using the `mechanize` library

        Return type: Mechanize browser object
    """
    def create_browser(self):
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(False)
        br.set_cookiejar(http.cookiejar.LWPCookieJar())
        br.addheaders=[('User-agent', Utils.user_agents())]
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        return br

    """
        Helper function to get current IP address
    """
    def get_ip(self):
        try:
            ip = None
            br = self.create_browser()
            ip = br.open('https://api.ipify.org/?format=text', timeout=1.5).read()
            br.close()
        except Exception as e:
            print(e)
        finally:
            if not self.alive:
                self.exit()
            return ip

    """
        Update the tor identity
    """
    def update_identity(self, pwd = None, recur=3):
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
                            Utils.call_shell_command('service network-manager restart', pwd)
                        sleep(1)
                if not ip:
                    self.restart_tor(pwd, recur-1)
            self.ip = ip
            print('Ip is', self.ip)
        except Exception as e:
            print(e)
