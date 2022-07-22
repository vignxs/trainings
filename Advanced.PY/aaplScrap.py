import requests
from bs4 import BeautifulSoup

i=('AAPL')
url =f"https://finance.yahoo.com/quote/{i}"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

r = requests.get(url, header)

soup = BeautifulSoup(r.text, "html.parser")

price = soup.find('span', {'class' : 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
name = soup.find('h1', {'class' : 'D(ib) Fz(18px)'}).text
change = soup.find('span', {'class' : 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}).text




print(f" Name {name} Price {price} Today Market Change {change}")