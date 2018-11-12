from datetime import datetime as dt
from zklibweb.client import ZkMaquine
from zklibweb.domain import Maquine

maq = Maquine('0.0.0.0', 'user', 'password')

client = ZkMaquine(maq)

if client.login():
    info = client.get_data(dt.now(), dt.now())
    client.close()
