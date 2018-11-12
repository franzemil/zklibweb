# ZKLIB web

*Selenium gecko driver is required*

This package allow access to attendace maquines using a web interface using selenium.

* 1. Instalation
  
```bash
pip install zklibweb
```

* 2. Use

```python
from datetime import datetime as dt
from zklibweb.client import ZkMaquine
from zklibweb.domain import Maquine

maq = Maquine('192.168.241.99', 'user', 'password')

client = ZkMaquine(maq)

if client.login():
    info = client.get_data(dt.now(), dt.now())
    client.close()
```
