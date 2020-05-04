from bizarre.tor import Tor

from os import path

if not path.exists('/usr/sbin/tor'):
    try:
        pass
    except KeyboardInterrupt:
        exit('Exiting ...')
    if all([not path.exists('/usr/sbin/tor')]):
        exit('Please Install Tor')

tor = Tor()

tor.restart_tor()
br = tor.create_browser()
url='https://api.covid19india.org/states_daily.json'

response = br.open(url)
print(response.read())

