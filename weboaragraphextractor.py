# extracting titles from website
import requests
from bs4 import BeautifulSoup

y=input("type your")
url = y
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')

for link in soup.find_all('p'):
    print(link.text)
