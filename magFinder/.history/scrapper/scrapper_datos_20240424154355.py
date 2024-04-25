import csv
import requests
from bs4 import BeautifulSoup

def scrape_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Assuming there might be multiple divs, use find_all
            div_principal = soup.find('div', class_='journalgrid')
            if div_principal:
                divs = div_principal.find_all('div')
                for div in divs:    
                    titles = div.find('h2')
                    if titles:
                        print(titles.get_text(strip=True))
                    else:
                        print('No h2 tag found in this div')
                    content = div.find('a')
                    if content:
                        print(content.get_text(strip=True))
        else:
            print(f"Failed to load page with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test with a specific URL
scrape_url('https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0')
