import os
from datetime import datetime as dt
from zklibweb.client import ZkMaquine
from zklibweb.domain import Maquine

host = os.getenv('ZKLIB_HOST_TEST')
username = os.getenv('ZKLIB_USER_TEST')
password = os.getenv('ZKLIB_PASSWORD_TEST')

maq = Maquine(host,  username, password)

client = ZkMaquine(maq, headless=True, firefox_path='/asdfas')

if client.login():
    info = client.get_data(dt.now(), dt.now())
    print(info)
    client.close()
