import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.scimagojr.com/journalrank.php"
TOTAL_PAGES = 584
CSV_FILE_PATH = 'revistas.csv'
URL_PREFIX = "https://www.scimagojr.com/"  # Prefijo del URL para completar los enlaces

def extraer_datos(url: str, csv_writer):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")

            tabla = soup.find('table')
            if tabla:
                filas = tabla.find_all('tr')
                for fila in filas:
                    celdas = fila.find_all('td')

                    if len(celdas) > 5:
                        link_element = celdas[1].find('a')
                        if link_element and 'href' in link_element.attrs:
                            link = URL_PREFIX + link_element['href'].strip()  # Completa el URL
                            titulo = link_element.text.strip()
                        else:
                            link = "No disponible"
                            titulo = "No disponible"

                        type_col = celdas[2].text.strip()
                        cuartil = celdas[3].find('span').text.strip() if celdas[3].find('span') else "No disponible"
                        h_index = celdas[4].text.strip()

                        # Escribir los datos en el archivo CSV
                        csv_writer.writerow([titulo, type_col, cuartil, h_index, link])
            else:
                print("Tabla no encontrada")
        else:
            print(f"Error al cargar la página: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al procesar la URL {url}: {e}")

# Abrir archivo CSV para escritura
with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir el encabezado del CSV
    writer.writerow(['Titulo', 'Type', 'SJR (Cuartil)', 'H_Index', 'Link'])

    # Procesar la primera página
    extraer_datos(BASE_URL + "?page=1&total_size=29165", writer)

    # Procesar el resto de las páginas
    for page_number in range(2, TOTAL_PAGES + 1):  # Empezando en 2 si la primera página ya fue procesada
        page_url = f"{BASE_URL}?page={page_number}&total_size=29165"
        extraer_datos(page_url, writer)
        time.sleep(1)  # Pausa de 1 segundo entre solicitudes
