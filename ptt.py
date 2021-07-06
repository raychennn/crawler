import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.ptt.cc/bbs/Stock/index.html')

soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.find_all('div', class_ = "title")
span = [s.text.strip() for s in spans]
print(span)