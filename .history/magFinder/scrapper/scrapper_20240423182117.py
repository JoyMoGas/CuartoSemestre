import requests
from bs4 import BeautifulSoup
import bs4

URL_PRINCIPAL = "https://www.scimagojr.com/journalrank.php#google_vignette"

response = requests.get(URL_PRINCIPAL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

tabla = soup.find('table')
#print(tabla)
titulos = tabla.find_all(['th', 'td'], class_="tit")
index = tabla.find_all(['th', 'td'])
for titulo in titulos:
    print(titulo.text.strip())

for titulo in titulos:
    link = titulo.find('a')  # Busca un elemento <a> dentro de cada título
    if link and 'href' in link.attrs:
        print(link['href'])  # Imprime el atributo href, que es el URL al que apunta el enlace
