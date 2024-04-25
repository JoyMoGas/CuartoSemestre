import requests
from bs4 import BeautifulSoup

def scrape_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the main 'journalgrid' div, assuming there might be multiple nested divs
            div_principal = soup.find('div', class_='journalgrid')
            if div_principal:
                divs = div_principal.find_all('div')
                for div in divs:    
                    titles = div.find('h2')
                    if titles:
                        print(titles.get_text(strip=True).upper())  # Print titles in uppercase
                    else:
                        print('No h2 tag found in this div')

                    # Use find_all to get all <a> tags within each div
                    links = div.find_all('a')
                    datas = div.find_all('p')
                    if links:
                        for link in links:
                            print(link.get_text(strip=True))  # Print all link texts
                    elif datas:
                        for data in datas:
                            print(data.get_text(strip=True))
                        
            else:
                print('No journalgrid div found')
        else:
            print(f"Failed to load page with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test with a specific URL
scrape_url('https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0')
