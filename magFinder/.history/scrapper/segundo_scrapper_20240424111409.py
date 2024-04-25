import requests
from bs4 import BeautifulSoup
import csv

CSV_ORIGINAL = 'revistas.csv'
CSV_NUEVO = 'datos_revista.csv'

def scrape_url(url):
    """ Función para hacer scraping en la URL dada y extraer títulos dentro de divs con clase 'journalgrid'. """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar el div con clase 'journalgrid'
            journal_grid = soup.find('div', class_='journalgrid')
            if journal_grid:
                # Extraer todos los elementos h2 dentro de este div
                titles = [h2.text.strip() for h2 in journal_grid.find_all('h2')]
                return titles
            else:
                return ['No journal grid found']
        else:
            print(f"Failed to retrieve content from {url}, status code {response.status_code}")
            return ['Failed to retrieve content']
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return ['Request failed']

def main():
    with open(CSV_INPUT_PATH, mode='r', newline='', encoding='utf-8') as file_in, \
        open(CSV_OUTPUT_PATH, mode='w', newline='', encoding='utf-8') as file_out:
        csv_reader = csv.reader(file_in)
        csv_writer = csv.writer(file_out)
        # Escribir el encabezado para el archivo de salida
        csv_writer.writerow(['URL', 'Titles'])

        next(csv_reader)  # Saltar el encabezado del archivo de entrada, si existe
        for row in csv_reader:
            if len(row) > 0:
                url = row[-1]  # Asumiendo que el URL es la última columna en tu CSV
                print(f"Scraping {url}")
                titles = scrape_url(url)
                for title in titles:
                    csv_writer.writerow([url, title])  # Escribir cada título en una nueva fila

if __name__ == '__main__':
    main()