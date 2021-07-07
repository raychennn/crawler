import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
save = []
r = requests.get('http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
if r.status_code == requests.codes.ok:  # 確認是否能取得資料
    soup = BeautifulSoup(r.text, 'lxml') # html.parser替代
    tables = soup.find_all('table',attrs = {'cellpadding' : '2'}) # attrs屬性搭配字典

    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date, value, price = [td.text for td in tr.find_all('td')] # list comprehension
            if date == '日期':
                continue
            data.append([date, value, price])
            print(data)

df = pd.DataFrame(data, columns = ['日期', '買賣超金額','台指期'])
df.to_csv('big_eight.csv')
            

    
    