import requests
from bs4 import BeautifulSoup

def scrape_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all div elements
            divs = soup.find_all('div')
            for div in divs:
                # Check if the div contains the specific h2 text
                if div.find('h2', text='Subject Area and Category'):
                    # Process the specific div with the heading "Subject Area and Category"
                    links = div.find_all('a')
                    print("Links in 'Subject Area and Category':")
                    for link in links:
                        text = link.get_text(strip=True)
                        href = link['href']
                        print(f"Text: {text}, URL: {href}")
                else:
                    # Process other divs
                    links = div.find_all('a')
                    if links:  # Check if there are any links
                        print("Links in other divs:")
                        for link in links:
                            text = link.get_text(strip=True)
                            href = link['href']
                            print(f"Text: {text}, URL: {href}")

        else:
            print(f"Failed to load page with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test with a specific URL
scrape_url('https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0')
