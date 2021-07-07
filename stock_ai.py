import requests
from bs4 import BeautifulSoup
import pprint


r = requests.get('https://chart.stock-ai.com/history?symbol=%5ETWII&resolution=D&from=1624816429&to=1625680429', verify = False)
data = r.json()
zp_data = zip(data['c'],data['h'], data['l'], data['o'], data['v'])
pprint.pprint(list(zp_data))