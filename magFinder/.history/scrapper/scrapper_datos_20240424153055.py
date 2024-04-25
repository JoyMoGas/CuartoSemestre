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

            divs = soup.find_all('div', class_='journalgrid')
            for div in divs:
                div.get_text(strip=True)
                print(div)
    except:
        print("Error")
