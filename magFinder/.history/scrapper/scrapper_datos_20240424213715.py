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
            
            input_element = soup.find('input', id='embed_code')
            if input_element:
                data['Embed Code'] = input_element['value']

            div_principal = soup.find('div', class_='journalgrid')
            if div_principal:
                divs = div_principal.find_all('div')
                for div in divs:
                    titles = div.find('h2')
                    if titles:
                        key = titles.get_text(strip=True).upper()  # Use title text as key in data dictionary
                        data[key] = []  # Initialize list to collect items under this title

                    links = div.find_all('a')
                    paragraphs = div.find_all('p')
                    
                    # Collecting links
                    for link in links:
                        data[key].append(link.get_text(strip=True))

                    # Collecting paragraph data
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
    # Determine all possible headers first if needed
    # This step could be omitted if the headers are known and static
    headers = set()
    with open(CSV_ORIGINAL, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            headers.update(scrape_url(row['Link']).keys())
    
    # Write headers to the CSV file
    with open(CSV_INFO, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(headers))
        writer.writeheader()

        # Re-open the original CSV to read URLs again and write data as it's scraped
        file.seek(0)  # Move the cursor back to the beginning of the file if reusing
        reader = csv.DictReader(file)
        for row in reader:
            data = scrape_url(row['Link'])
            writer.writerow(data)
            time.sleep(1)  # Wait for one second between requests

# Run the scraping process
read_urls_and_scrape()
