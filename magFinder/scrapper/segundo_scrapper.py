import csv
import requests
from bs4 import BeautifulSoup

# Rutas de los archivos CSV de entrada y salida
CSV_INPUT_PATH = 'revistas.csv'
CSV_OUTPUT_PATH = 'datos_revista.csv'

def scrape_url(url):
    """ Función para hacer scraping en la URL dada y extraer datos de los divs con clase 'journalgrid'. """
    data = []
    headers = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar todos los divs con clase 'journalgrid'
            journal_grids = soup.find_all('div', class_='journalgrid')
            for journal_grid in journal_grids:
                # Extraer el título h2
                h2 = journal_grid.find('h2')
                if h2:
                    headers.append(h2.text.strip())
                # Extraer el texto de todos los enlaces y párrafos
                links = [a.text.strip() for a in journal_grid.find_all('a') if a.text.strip()]
                three = [ul.text.strip() for ul in journal_grid.find_all('ul') if ul.text.strip()]
                paragraphs = [p.text.strip() for p in journal_grid.find_all('p')]
                data.append(links + paragraphs)
        else:
            print(f"Failed to retrieve content from {url}, status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
    return headers, data

def main():
    with open(CSV_INPUT_PATH, mode='r', newline='', encoding='utf-8') as file_in, \
        open(CSV_OUTPUT_PATH, mode='w', newline='', encoding='utf-8') as file_out:
        csv_reader = csv.reader(file_in)
        csv_writer = csv.writer(file_out)
        
        # Asignar que solo obtenemos headers del primer URL
        headers_set = False
        headers = []

        next(csv_reader)  # Saltar el encabezado del archivo de entrada, si existe
        for row in csv_reader:
            if len(row) > 0:
                url = row[-1]  # Asumiendo que el URL está en la última columna
                print(f"Scraping {url}")
                current_headers, data = scrape_url(url)
                
                if not headers_set:  # Establecer los encabezados solo una vez
                    headers = ['URL'] + current_headers  # Asumiendo que los títulos de h2 son los encabezados
                    csv_writer.writerow(headers)
                    headers_set = True
                
                # Escribir la información extraída para cada 'journalgrid' div
                for entry in data:
                    row_data = [url] + entry
                    csv_writer.writerow(row_data)

if __name__ == '__main__':
    main()
