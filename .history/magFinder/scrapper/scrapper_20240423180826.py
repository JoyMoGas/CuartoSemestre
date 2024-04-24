import requests
from bs4 import BeautifulSoup
import bs4

URL_PRINCIPAL = "https://www.scimagojr.com/journalrank.php#google_vignette"

response = requests.get(URL_PRINCIPAL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

print(soup)

