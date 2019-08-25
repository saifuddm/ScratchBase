import requests
from bs4 import BeautifulSoup
from pprint import pprint


exportFile = open("NikeData.txt",'w+')
exportSoup = open("nikeDataBetter.txt", 'w+')
exportLatestProduct = open("LatestProduct.txt",'w+')
BASE_URL = 'https://www.nike.com/ca/w/mens-shoes-nik1zy7ok?sort=newest'

r = requests.get(BASE_URL)
exportFile.write(r.content)

soup = BeautifulSoup(r.content,'html.parser')
exportSoup.write(soup.prettify().encode('utf-8'))
#Extract Picture and URL
picture = soup.find_all("a",class_="product-card__img-link-overlay")

#Extract Price
price = soup.find_all(attrs={"data-test":"product-price"})
#Extract Product Title
title = soup.find_all(attrs={"class":"product-card__title"})

for entry in range(len(title)):
    exportLatestProduct.write(title[entry].text +","+ price[entry].text +','+picture[entry].attrs.get('href', 'CHECK')+ '\n')

exportFile.close()
exportSoup.close()
exportLatestProduct.close()