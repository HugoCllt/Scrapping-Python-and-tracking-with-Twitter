import bs4
from bs4 import BeautifulSoup
import requests

url = 'https://howrare.is/drops'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
i = -1
j = 0
dicDate={}

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
        
        name = row.findAll('td', class_='')[0].text.strip()
        time = row.findAll('td', class_='')[2].text.strip()
        count = row.findAll('td', class_='')[-3].text.strip()
        price = row.findAll('td', class_='')[-2].text.strip().split(' ')[0]
        liens = row.findAll('td', class_='')[1]
        lien = str(row.findAll('a')[-1]).split('href="')[1].split('" target')[0]
        
        date = dicDate[i]
        
        print(f'''
              name : {name}
              liens : {lien}
              time : {time}
              count : {count}
              price : {price}
              date : {date}
              ''')
print(i)
print(j)
#compter le nombre de tableau, compter le nombre de date, assigner une date par tableau
