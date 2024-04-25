import csv
import requests
from bs4 import BeautifulSoup

# Rutas de los archivos CSV de entrada y salida
CSV_INPUT_PATH = 'revistas.csv'
CSV_OUTPUT_PATH = 'datos_revista.csv'

def scrape_url(url):
    """ Función para hacer scraping en la URL dada y extraer datos relevantes de divs. """
    data = []
    headers = ["Subject Area and category", "Publisher", "ISSN"]  # Encabezados relevantes, excepto URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar todos los divs con clase 'journalgrid'
            journal_grids = soup.find_all('div', class_='journalgrid')
            for journal_grid in journal_grids:
                h2 = journal_grid.find('h2')
                if h2 and any(header in h2.text.strip() for header in headers):
                    # Extraer los datos si el h2 contiene alguno de los encabezados válidos
                    content = {
                        'h2': h2.text.strip(),
                        'links': [a.text.strip() for a in journal_grid.find_all('a')],
                        'paragraphs': [p.text.strip() for p in journal_grid.find_all('p')],
                        'lists': [ul.text.strip() for ul in journal_grid.find_all('ul')]
                    }
                    data.append(content)
        else:
            print(f"Failed to retrieve content from {url}, status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
    return data

def main():
    with open(CSV_INPUT_PATH, mode='r', newline='', encoding='utf-8') as file_in, \
         open(CSV_OUTPUT_PATH, mode='w', newline='', encoding='utf-8') as file_out:
        csv_reader = csv.reader(file_in)
        csv_writer = csv.writer(file_out)
        # Escribir encabezados en el archivo de salida
        csv_writer.writerow(['Sitio web'] + ["Subject Area and category", "Publisher", "ISSN"])  # Encabezados, incluyendo URL

        next(csv_reader)  # Saltar el encabezado del archivo de entrada, si existe
        for row in csv_reader:
            if len(row) > 0:
                url = row[-1]  # Asumiendo que el URL está en la última columna
                print(f"Scraping {url}")
                data = scrape_url(url)
                
                # Escribir la información extraída para cada 'journalgrid' div relevante
                for entry in data:
                    row_data = [url, entry['h2'], "; ".join(entry['links']), "; ".join(entry['paragraphs']), "; ".join(entry['lists'])]
                    csv_writer.writerow(row_data)

if __name__ == '__main__':
    main()
