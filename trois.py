import bs4
from bs4 import BeautifulSoup
import requests

url = 'https://howrare.is/drops'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

tableau = soup.find_all('table')

for t in tableau.find_all('tbody'):
    rows = t.find_all('tr')
    for row in rows:
        name = row.findAll('td', class_='')[0].text.strip()
        time = row.findAll('td', class_='')[2].text.strip()
        count = row.findAll('td', class_='')[4].text.strip()
        price = row.findAll('td', class_='')[5].text.strip().split(' ')[0]
        print(f'''
              name : {name}
              time : {time}
              count : {count}
              price : {price}
              ''')
    
    
    
