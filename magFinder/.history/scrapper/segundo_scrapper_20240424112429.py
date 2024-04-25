import csv
import requests
from bs4 import BeautifulSoup

# Rutas de los archivos CSV de entrada y salida
CSV_INPUT_PATH = 'revistas.csv'
CSV_OUTPUT_PATH = 'datos_revista.csv'

def scrape_url(url):
    """ Función para hacer scraping en la URL dada y extraer datos de los divs con clase 'journalgrid'. """
    data = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar todos los divs con clase 'journalgrid'
            journal_grids = soup.find_all('div', class_='journalgrid')
            for journal_grid in journal_grids:
                entry = {}
                # Extraer el título h2
                h2 = journal_grid.find('h2')
                if h2:
                    entry['title'] = h2.text.strip()
                else:
                    entry['title'] = 'No Title Found'

                # Extraer el texto de todos los enlaces
                entry['links'] = [a.text.strip() for a in journal_grid.find_all('a') if a.text.strip()]
                entry['paragraphs'] = [p.text.strip() for p in journal_grid.find_all('p')]
                
                data.append(entry)
        else:
            print(f"Failed to retrieve content from {url}, status code {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return []
    return data

def main():
    with open(CSV_INPUT_PATH, mode='r', newline='', encoding='utf-8') as file_in, \
        open(CSV_OUTPUT_PATH, mode='w', newline='', encoding='utf-8') as file_out:
        csv_reader = csv.reader(file_in)
        csv_writer = csv.writer(file_out)
        
        # Leer el archivo y obtener los URLs
        next(csv_reader)  # Saltar el encabezado del archivo de entrada, si existe
        for row in csv_reader:
            if len(row) > 0:
                url = row[-1]  # Asumiendo que el URL está en la última columna
                print(f"Scraping {url}")
                data = scrape_url(url)
                
                # Escribir la información extraída para cada 'journalgrid' div
                for entry in data:
                    row_data = [url, entry['title']] + entry['links'] + entry['paragraphs']
                    csv_writer.writerow(row_data)  # Escribir la URL, el título, los enlaces y los párrafos en una fila

if __name__ == '__main__':
    main()
