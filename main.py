import bs4
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse

#test
url = 'https://howrare.is/drops'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}

html = requests.get(url,headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')
i = -1
j = 0
dicDate={}
data=[]

titles = soup.findAll('p', class_ = 'title')
for title in titles:
    titre = title.text.strip()
    dicDate[j] = titre
    j = j+1


tableau = soup.findAll('table')
for eacht in tableau:
    i = i+1
    for t in eacht.findAll('tbody'):
        rows = t.findAll('tr')
    for row in rows:
        d=dict()
        d['name'] = row.findAll('td', class_='')[0].text.strip()
        d['time'] = row.findAll('td', class_='')[2].text.strip()
        d['count'] = row.findAll('td', class_='')[-3].text.strip()
        d['price'] = row.findAll('td', class_='')[-2].text.strip().split(' ')[0]
        d['lien'] = str(row.findAll('a')[-1]).split('href="')[1].split('" target')[0]
        
        d['date'] = dicDate[i]
        
        data.append(d)

with open('classement.json','w') as f:
    json.dump(data,f,indent=4)
