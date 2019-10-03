import urllib
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os

course = "3SK3"
folder = "Project2"
url = 'http://stoldark.com/McMaster/'+course+'/'+folder+'/'
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
listLinks = soup.find_all("a")
result = urllib.urlopen(url)
filename = []
for i in range(len(listLinks)):
    if (listLinks[i].text.find('.') != -1):
        filename.append(listLinks[i].text)
basePath= '/Users/murtmac/Documents/EngineeringYear4-2006/'+course+'/'
myPath = basePath + folder
os.mkdir(myPath)
for k in range(len(filename)):
    fullfilename = os.path.join(myPath, filename[k])
    urllib.urlretrieve(url+filename[k], fullfilename)