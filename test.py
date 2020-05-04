from bizarre.tor import Tor

from os import path

if not path.exists('/usr/sbin/tor'):
    try:
        youtube_views.installTor()
    except KeyboardInterrupt:
        exit('Exiting ...')
    if all([not path.exists('/usr/sbin/tor')]):
        exit('Please Install Tor')

tor = Tor()

tor.restart_tor()