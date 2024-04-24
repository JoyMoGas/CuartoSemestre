import requests
from bs4 import BeautifulSoup
import bs4

URL_PRINCIPAL = "https://www.scimagojr.com/journalrank.php#google_vignette"
TOTAL_PAGES = 584

def extraer_datos(url: str):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    tabla = soup.find('table')

    if (tabla):
        filas = tabla.find_all('tr')

        for fila in filas:
            celdas = fila.find_all('td')

            if len(celdas) > 5:
                titulo = celdas[1].text.strip()
                type_col = celdas[2].text.strip()
                cuartil = (celdas[3].find('span')).text.strip()
                h_index = celdas[4].text.strip()

                print(f"Titulo: {titulo:<45} | Tipo: {type_col:<13} | Cuartil: {cuartil} | {h_index}")
                #print(titulo, type_col, h_index)
    else:
        print("Tabla no encontrada")

extraer_datos(URL_PRINCIPAL)

# Suponiendo que la paginación se maneja con enlaces directos a cada página numerada:
soup = BeautifulSoup(requests.get(URL_PRINCIPAL).text, "html.parser")
paginacion = soup.find('div', class_='pagination')  # Cambia esto según sea necesario
if paginacion:
    enlaces = paginacion.find_all('a')
    urls_paginas = [enlace['href'] for enlace in enlaces if 'href' in enlace.attrs]

    for url in urls_paginas:
        extraer_datos(url)  # Vuelve a utilizar la función para cada página