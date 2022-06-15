import requests
from bs4 import BeautifulSoup

c = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_6?crid=BVYASC0FZWEY&keywords=iphone&qid=1654171881&sprefix=phone%2Caps%2C435&sr=8-6"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70"}

page = requests.get(c, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

title = soup.find(id="productTitle").get_text()
print(title.strip())

pirce = soup.find(class_="a-price-whole").get_text()
print(pirce)