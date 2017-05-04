
from bs4 import BeautifulSoup
import requests

url = requests.get("http://www.espn.com/nba//statistics/player/_/stat/scoring/sort/points")

url = url.text
players = []
soup = BeautifulSoup(url, "lxml")
pageList = ["http://www.espn.com/nba//statistics/player/_/stat/scoring/sort/points"]
newSoup = BeautifulSoup(url, "lxml")
done = False
while done == False:
    for link in pageList:
        isNew = False
        newUrl = requests.get(link)
        newSoup = BeautifulSoup(newUrl.text, "lxml")
        for i in newSoup.find_all("a"):
            url = i.get("href")
            if "www.espn.com/nba/statistics/player/_/stat/scoring/sort/points/qualified/false/count/" in url and url not in pageList and ("http:" + url) not in pageList:
                if "http" in url:   
                    pageList.append(url)
                else: pageList.append("http:" + url)
                isNew = True
    if isNew == 0:
        done = True
            
    
for link in pageList:
    url = requests.get(link)
    soup = BeautifulSoup(url.text,"lxml")
    for i in soup.find_all("a"):
        if "http://www.espn.com/nba/player/_/id/" in i.get('href'):
            players.append(i.get('href'))