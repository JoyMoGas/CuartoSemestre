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
        'URL_IMAGEN': ''
    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            journalgrid = soup.find('div', class_='journalgrid')
            if journalgrid:
                elements = journalgrid.find_all(['a', 'p'])
                if len(elements) >= 6:  # Adjusted number of elements to match the new fields count
                    data.update({
                        'COUNTRY': elements[0].get_text(strip=True),
                        'SUBJECT AREA AND CATEGORY': elements[1].get_text(strip=True),
                        'PUBLISHER': elements[2].get_text(strip=True),
                        'H-INDEX': elements[3].get_text(strip=True),
                        'PUBLICATION TYPE': elements[4].get_text(strip=True),
                        'ISSN': elements[5].get_text(strip=True),
                        'COVERAGE': elements[6].get_text(strip=True)
                    })
            # Attempt to get the image URL from the embed code input
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
