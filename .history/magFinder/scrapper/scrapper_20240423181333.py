import requests
from bs4 import BeautifulSoup
import bs4

URL_PRINCIPAL = "https://www.scimagojr.com/journalrank.php#google_vignette"

response = requests.get(URL_PRINCIPAL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

tabla = soup.find('table')
#print(tabla)
titulos = tabla.find_all(['th'])
print(titulos)
