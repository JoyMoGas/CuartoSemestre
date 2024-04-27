import csv
import requests
from bs4 import BeautifulSoup
import time

CSV_ORIGINAL = 'revistas.csv'
CSV_INFO = 'revista_info.csv'

def scrape_url(url: str):
    print(f"Scraping URL: {url}")
    data = {
        'URL': url,
        'COUNTRY': '',
        'SUBJECT AREA AND CATEGORY': '',
        'PUBLISHER': '',
        'H-INDEX': '',
        'PUBLICATION TYPE': '',
        'ISSN': '',
        'COVERAGE': '',
        'URL_IMAGEN': ''  # Supongo que seguimos tomando el URL de la imagen de 'embed_code'
    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for div in soup.find_all('div'):
                header_text = div.find('h2').get_text(strip=True) if div.find('h2') else ""
                content = div.find('p')

                if header_text == "Country":
                    data['COUNTRY'] = content.find('a').get_text(strip=True) if content and content.find('a') else "No country info"
                elif header_text == "Subject Area and Category":
                    if content:
                        areas = content.find_all('a')
                        data['SUBJECT AREA AND CATEGORY'] = ', '.join([area.get_text(strip=True) for area in areas])
                elif header_text == "Publisher":
                    data['PUBLISHER'] = content.find('a').get_text(strip=True) if content and content.find('a') else "No publisher info"
                elif header_text == "H-Index":
                    data['H-INDEX'] = content.get_text(strip=True) if content else "No H-Index"
                elif header_text == "Publication type":
                    data['PUBLICATION TYPE'] = content.get_text(strip=True) if content else "No publication type"
                elif header_text == "ISSN":
                    data['ISSN'] = content.get_text(strip=True) if content else "No ISSN"
                elif header_text == "Coverage":
                    data['COVERAGE'] = content.get_text(strip=True) if content else "No coverage"

            input_element = soup.find('input', id='embed_code')
            if input_element and 'value' in input_element.attrs:
                data['URL_IMAGEN'] = input_element['value']
        else:
            print(f"Failed to load page with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def read_urls_and_scrape():
    with open(CSV_ORIGINAL, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        with open(CSV_INFO, mode='w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['URL', 'COUNTRY', 'SUBJECT AREA AND CATEGORY', 
                          'PUBLISHER', 'H-INDEX', 'PUBLICATION TYPE',
                          'ISSN', 'COVERAGE', 'URL_IMAGEN']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                data = scrape_url(row['Link'])
                writer.writerow(data)
                time.sleep(1)  # Wait for one second between requests

# Run the scraping process
read_urls_and_scrape()