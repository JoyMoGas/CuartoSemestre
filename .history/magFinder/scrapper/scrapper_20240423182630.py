import requests
from bs4 import BeautifulSoup
import bs4

URL_PRINCIPAL = "https://www.scimagojr.com/journalrank.php#google_vignette"

response = requests.get(URL_PRINCIPAL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

tabla = soup.find('table')

if (tabla):
    filas = tabla.find_all('tr')

    for fila in filas:
        celdas = fila.find_all('td')

        if len(celdas) > 5:
            titulo = celdas[0].text.strip()
            type_col = celdas[1].text.strip()
            h_index = celdas[3].text.strip()

            print(titulo, type_col, h_index)
else:
    print("Tabla no encontrada")