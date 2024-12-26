import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Meta-Quest-3S-128GB-All-One/dp/B0DDK1WM9K/?_encoding=UTF8&th=1"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text,"lxml")
print(soup)