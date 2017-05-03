# -*- coding: utf-8 -*-
"""

@author: Moritz
"""

from bs4 import BeautifulSoup
import requests

url = requests.get('http://www.espn.com/nba/statistics/player/_/stat/scoring/sort/points/qualified/false')

# print(url.text) 

soup = BeautifulSoup(url.text, "lxml")
players = []
pages = []
pretty_soup = soup.prettify()

        
for j in soup.find_all('a'):
    if "www.espn.com/nba/statistics/player/_/stat/scoring/sort/points/qualified/false/count" in j.get('href'):
        pages.append(j.get('href'))
        
for i in soup.find_all('a'):
    if "www.espn.com/nba/player/_/id" in i.get('href'):
        players.append(i.get('href'))
        
        
print(len(pages))