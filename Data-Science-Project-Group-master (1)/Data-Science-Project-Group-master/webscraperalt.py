
from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import zip_longest


url = requests.get("http://www.espn.com/nba//statistics/player/_/stat/scoring/sort/points")
soup = BeautifulSoup(url.text, "lxml")
newSoup = soup

players = []
pageList = ["http://www.espn.com/nba//statistics/player/_/stat/scoring/sort/points"]
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
            statPage = i.get('href')[:30] + "/stats" + i.get('href')[30:]
            players.append(statPage)

testset = players[:2]

data = []

for player in testset:
    trows = []
    doc = requests.get(player)
    soup = BeautifulSoup(doc.text, "lxml")
    for meta in soup.find_all("meta"):
        if meta.has_attr("property"):
            if "og:title" in meta.get("property"):
                name = meta['content']
    for tr in soup.find_all("tr"):
        tdata = []
        for td in tr:
            tdata.append(td.string)
        trows.append(tdata)
    trows = trows[3:]
    pEntry = {'name':name}
    z = zip_longest(trows[1], trows[2], trows[3], fillvalue="error")
    for x in z:
        print(x)
            




            