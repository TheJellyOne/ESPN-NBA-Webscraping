# Webscraping NBA Stats on ESPN

Contributers:
+ Moritz Droste
+ Jiali Huang
+ Russell Kim
+ Chris Bell

## This is a beginner webscraper taking data from NBA players on ESPN.

To-Do List
+ All done


### Code and Walkthrough

We went through this project using python and the BeautifulSoup library. Therefore, we first had to import all the necessary libraries into python.

```
from bs4 import BeautifulSoup
import requests
import pandas 
```

Requests is a library used to request the html documents from webpages. Pandas is a library for creating and manipulating dataframes, which is how we store the data we get before putting it into a mySQL table.

Then, we dive right in and use requests to get the webpages. 

```
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
```

The other major part of our project was getting all of the data from the pages and sort it into a dataframe that was easily readable. To do this, we used the pandas library. 

```
testset = players

data = []
for player in testset:
    trows = []
    doc = requests.get(player)
    soup = BeautifulSoup(doc.text, "lxml")
    for tr in soup.find_all("tr"):
        tdata = []
        for td in tr:
            tdata.append(td.string)
        trows.append(tdata)
    trows = trows[3:]
    numObs = int(len(trows)/3)
    trows1 = trows[1:numObs]
    trows2 = trows[numObs + 1:2*numObs]
    trows3 = trows[2*numObs + 1:]
    for meta in soup.find_all('meta'):
        if meta.has_attr("property"):
            if "og:title" in meta.get("property"):
                name = meta['content']
    for l in range(numObs-3):
        observation={}
        observation["Name"] = name
        for i in range(len(trows1[0])):
            observation[trows1[0][i]] = trows1[l+1][i]
        for j in range(len(trows2[0])):
            if str(trows2[0][j]) in list(observation.keys()):
                observation[str(trows2[0][j]) + " Season Total"] = trows2[l+1][j]
            else:
                observation[trows2[0][j]] = trows2[l+1][j]
        for k in range(len(trows3[0])):
            observation[trows3[0][k]] = trows3[l+1][k]
        data.append(observation)

csv = pd.DataFrame(data)
csv.to_csv("out.csv")
```

At the end, we just put all of the data into a csv so that we could make the transfer to mySQL easier. 