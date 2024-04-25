import csv
import requests
from bs4 import BeautifulSoup

ARCHIVO_ORIGINAL = 'revistas.csv'
ARCHIVO_NUEVO = 'info_revistas.csv'

def scrape_url(url:str):
    data = []
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            divs = soup.find('div', class_='journalgrid')
            for div in divs:
                titles = div.find('h2')
                if titles:
                    print(titles)
                else:
                    print('Fallo al encontrar los h2')
    except:
        print("Error")

scrape_url('https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0')
