import csv
import requests
from bs4 import BeautifulSoup
import time

CSV_ORIGINAL = 'revistas.csv'
CSV_INFO = 'revista_info.csv'

def scrape_url(url: str):
    print(f"Scraping URL: {url}")
    data = {
        'TITLE': '',
        'URL': url,
        'COUNTRY': '',
        'SUBJECT AREA AND CATEGORY': '',
        'PUBLISHER': '',
        'H-INDEX': '',
        'PUBLICATION TYPE': '',
        'ISSN': '',
        'COVERAGE': '',
        'URL_IMAGEN': '',
        'SCOPE': ''
    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the main <h1> title if available
            h1_tag = soup.find('h1')
            if h1_tag:
                data['TITLE'] = h1_tag.get_text(strip=True)
            else:
                data['TITLE'] = 'No Title Found'
            
            # Look for scope information specifically
            for div in soup.find_all('div', class_='fullwidth'):
                h2_tag = div.find('h2')
                if h2_tag and 'scope' in h2_tag.get_text(strip=True).lower():
                    data['SCOPE'] = div.get_text(strip=True, separator=' ').strip()

            # Look for other data
            for div in soup.find_all('div'):
                header_text = div.find('h2').get_text(strip=True) if div.find('h2') else ""
                content = div.find('p')

                if header_text == "Country":
                    data['COUNTRY'] = content.get_text(strip=True) if content else "No country info"
                elif header_text == "Subject Area and Category":
                    areas = content.find_all('a')
                    data['SUBJECT AREA AND CATEGORY'] = ', '.join([a.get_text(strip=True) for a in areas])
                elif header_text == "Publisher":
                    data['PUBLISHER'] = content.get_text(strip=True) if content else "No publisher info"
                elif header_text == "H-Index":
                    data['H-INDEX'] = content.get_text(strip=True) if content else "No H-Index"
                elif header_text == "Publication type":
                    data['PUBLICATION TYPE'] = content.get_text(strip=True) if content else "No publication type"
                elif header_text == "ISSN":
                    data['ISSN'] = content.get_text(strip=True) if content else "No ISSN"
                elif header_text == "Coverage":
                    data['COVERAGE'] = content.get_text(strip=True) if content else "No coverage"

            input_element = soup.find('input', id='embed_code')
            if input_element:
                data['URL_IMAGEN'] = input_element['value']

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def read_urls_and_scrape():
    existing_urls = set()
    try:
        with open(CSV_INFO, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                existing_urls.add(row['URL'])
    except FileNotFoundError:
        print("Existing data file not found, creating a new one.")

    with open(CSV_ORIGINAL, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        with open(CSV_INFO, mode='a', newline='', encoding='utf-8') as outfile:
            fieldnames = ['TITLE', 'URL', 'COUNTRY', 'SUBJECT AREA AND CATEGORY',
                          'PUBLISHER', 'H-INDEX', 'PUBLICATION TYPE',
                          'ISSN', 'COVERAGE', 'URL_IMAGEN', 'SCOPE']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            if not existing_urls:
                writer.writeheader()

            for row in reader:
                if row['Link'] in existing_urls:
                    print("Archivo ya agregado:", row['Link'])
                    continue
                data = scrape_url(row['Link'])
                writer.writerow(data)
                existing_urls.add(row['Link'])
                time.sleep(1)

# Run the scraping process
read_urls_and_scrape()
