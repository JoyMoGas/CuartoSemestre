import csv
import requests
from bs4 import BeautifulSoup
import time

CSV_ORIGINAL = 'revistas.csv'
CSV_INFO = 'revista_info.csv'

def scrape_url(url: str):
    print(f"Analizando: {url}")  # Print the URL being analyzed
    data = {'URL': url}  # Start with URL to identify source in CSV
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Scrape the data as before
            input_element = soup.find('input', id='embed_code')
            if input_element:
                data['Embed Code'] = input_element['value']

            div_principal = soup.find('div', class_='journalgrid')
            if div_principal:
                divs = div_principal.find_all('div')
                for div in divs:
                    titles = div.find('h2')
                    if titles:
                        key = titles.get_text(strip=True).upper()
                        data[key] = []

                    links = div.find_all('a')
                    paragraphs = div.find_all('p')
                    
                    for link in links:
                        data[key].append(link.get_text(strip=True))

                    for paragraph in paragraphs:
                        data[key].append(paragraph.get_text(strip=True))
            else:
                print('No journalgrid div found')
        else:
            print(f"Failed to load page with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def read_urls_and_scrape():
    scraped_data = []
    headers = {'URL', 'Embed Code'}  # Initialize with known headers
    with open(CSV_ORIGINAL, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = scrape_url(row['Link'])
            scraped_data.append(data)
            headers.update(data.keys())
            time.sleep(1)  # Wait for one second between requests

    # Write the scraped data to CSV
    with open(CSV_INFO, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(headers))
        writer.writeheader()
        for data in scraped_data:
            writer.writerow(data)

# Run the scraping process
read_urls_and_scrape()
