import requests
from bs4 import BeautifulSoup

root_url = 'https://www.ptt.cc/bbs/Stock/'

r = requests.get('https://www.ptt.cc/bbs/Stock/index.html')

soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.find_all('div', class_ = "title")
span = [s.text.strip() for s in spans]

for span in spans:
	url = root_url + span.find('a').get('href')
	print(url)
	print(span.text)

with open('test.csv', 'w', encoding = 'utf-8-sig') as f:
	for span in spans:
		f.write(span.text + '\n' + url)