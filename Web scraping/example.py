import requests
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
c=r.content

soup = BeautifulSoup(c, "html.parser")

title = soup.find_all("p",{"class":"description"})
item = title[0].get_text()

print(item.index(","))