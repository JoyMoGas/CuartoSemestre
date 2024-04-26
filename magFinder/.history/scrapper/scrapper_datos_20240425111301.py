import csv
import requests
from bs4 import BeautifulSoup
import time

CSV_ORIGINAL = 'revistas.csv'
CSV_INFO = 'revista_info.csv'

def scrape_url(url: str):
    print(f"Scraping URL: {url}")
    data = {'URL': url}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data['Embed Code'] = soup.find('input', id='embed_code')['value'] if soup.find('input', id='embed_code') else 'Not found'

            journalgrid = soup.find('div', class_='journalgrid')
            if journalgrid:
                for div in journalgrid.find_all('div'):
                    title_elements = div.find_all('h2')
                    for title in title_elements:
                        key = title.get_text(strip=True).upper()  # Use as key, but we will not use these as headers in CSV
                        data[key] = []
                        # Gather all links and paragraphs under each title
                        for element in div.find_all(['a', 'p']):
                            data[key].append(element.get_text(strip=True))
            else:
                print('No "journalgrid" div found')
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
            fieldnames = ['URL', 'Embed Code', 'Additional Info']  # Define your fieldnames for the CSV
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                data = scrape_url(row['Link'])
                # Assuming you want to flatten data from different h2 sections into one string per URL
                additional_info = {k: ', '.join(v) for k, v in data.items() if k not in ['URL', 'Embed Code']}
                data['Additional Info'] = str(additional_info)
                writer.writerow({field: data.get(field, '') for field in fieldnames})
                time.sleep(1)  # Wait for one second between requests

# Run the scraping process
read_urls_and_scrape()
