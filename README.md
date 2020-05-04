# tor-wrapper-python
A python wrapper for tor to browse sites anonymously.

## Development

1. Install package using pip
```shell
 pip install git+ssh://git@github.com/vivekkumar2696/tor-wrapper-python.git
```
2. Sample python code
```python
from bizarre.tor import Tor
tor = Tor()
tor.restart_tor()
br = tor.create_browser()
url='https://api.covid19india.org/states_daily.json'

response = br.open(url)
print(response.read())
```
create_browser() returns a mechanize._mechanize.Browser object

#### Update Identity

```python
from bizarre.tor import Tor
tor = Tor()
tor.update_identity()
```