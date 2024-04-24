import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.scimagojr.com/journalrank.php"
TOTAL_PAGES = 584

def extraer_datos(url: str):
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
                        titulo = celdas[1].text.strip()
                        type_col = celdas[2].text.strip()
                        cuartil = (celdas[3].find('span')).text.strip()
                        h_index = celdas[4].text.strip()

                        print(f"Titulo: {titulo:<45} | Tipo: {type_col:<13} | Cuartil: {cuartil} | H-index: {h_index}")
            else:
                print("Tabla no encontrada")
        else:
            print(f"Error al cargar la página: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al procesar la URL {url}: {e}")

# Procesa la primera página
extraer_datos(BASE_URL + "?page=1&total_size=29165")

# Procesa el resto de las páginas
for page_number in range(2, TOTAL_PAGES + 1):  # Empezando en 2 si la primera página ya fue procesada
    page_url = f"{BASE_URL}?page={page_number}&total_size=29165"
    extraer_datos(page_url)
    time.sleep(1)  # Pausa de 1 segundo entre solicitudes
