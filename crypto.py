import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

crypto = []
rise_count = []
drop_count = []
total_coin = []
sequence = []
biggest = []

r = requests.get('https://shrtm.nu/ZEYu')
new = r.json()
data = new['data']
for block in data:
    if 'name' in block:
        name = block.get('name')
        crypto.append(name)

    if 'rise_count' in block:
        num1 = block.get('rise_count')
        rise_count.append(num1)

    if 'drop_count' in block:
        num2 = block.get('drop_count')
        drop_count.append(num2)
        
    if 'total_coin' in block:
        num3 = block.get('total_coin')
        total_coin.append(num3)


zipped = zip(crypto, rise_count, drop_count, total_coin)
df = pd.DataFrame(zipped, columns = ['板塊','上漲數','下跌數','總數量'])
df.to_excel('report.xlsm')








    



