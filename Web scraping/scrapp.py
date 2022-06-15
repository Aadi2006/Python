#Importing required libraries
import requests
from bs4 import BeautifulSoup

#Getting website
r=requests.get('https://pythonizing.github.io/data/example.html')
c=r.content

#Getting html code to look good
soup = BeautifulSoup(c, "html.parser")
prettysoup = soup.prettify()

#Getting divs with class of cities
all = soup.find_all("div", {"class": "cities"})
cities=[]

#Printing all of the H2 and P tags beautifully
for item in all:
    print(item.find('h2').text)
    print(f'{item.find_all("p")[0].text}\n')

