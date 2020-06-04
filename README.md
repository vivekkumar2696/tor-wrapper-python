# tor-wrapper-python
A python wrapper for tor to browse sites anonymously.

## Development
##### Prerequisites:-
1. Linux based OS
2. Tor must be installed on the system.
    ```shell
    $ echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
    $ apt install tor
    ```

##### Sample steps
1. Install package using pip
```shell
 pip install git+ssh://git@github.com/vivekkumar2696/tor-wrapper-python.git
```
2. Sample python code
```python
from bizarre.tor import Tor
sudo_pwd = None # Optional. If not specified, there would be a prompt later to ask for password

tor = Tor()
tor.restart_tor(sudo_pwd)
br = tor.create_browser()
url='https://api.covid19india.org/states_daily.json'

response = br.open(url)
print(response.read())
```
create_browser() returns a mechanize._mechanize.Browser object

##### Update Identity

```python
from bizarre.tor import Tor
sudo_pwd = None # Optional. If not specified, there would be a prompt later to ask for password

tor = Tor()
tor.update_identity(sudo_pwd)
```
