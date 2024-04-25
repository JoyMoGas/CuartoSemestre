import csv
import requests
from bs4 import BeautifulSoup

# Rutas de los archivos CSV de entrada y salida
CSV_INPUT_PATH = 'revistas.csv'
CSV_OUTPUT_PATH = 'datos_revista.csv'

def scrape_url(url):
    """ Función para hacer scraping en la URL dada y extraer datos específicos. """
    data = {
        'Sitio web': url,
        'Subject Area and category': '',
        'Publisher': '',
        'ISSN': '',
        'Widget': ''
    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Estos selectores son ejemplos. Debes ajustarlos según el HTML de tu objetivo.
            # Suponiendo que estos datos están en párrafos o divs con clases específicas:
            data['Subject Area and category'] = soup.find('div', class_='subject-area').text.strip() if soup.find('div', class_='subject-area') else 'Not found'
            data['Publisher'] = soup.find('div', class_='publisher').text.strip() if soup.find('div', class_='publisher') else 'Not found'
            data['ISSN'] = soup.find('div', class_='issn').text.strip() if soup.find('div', class_='issn') else 'Not found'
            
            # Ejemplo de cómo podrías extraer un widget o algún otro elemento único
            widget = soup.find('div', class_='widget')
            data['Widget'] = widget.text.strip() if widget else 'Not found'
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
        
        # Escribir el encabezado en el archivo de salida
        csv_writer.writerow(['Sitio web', 'Subject Area and category', 'Publisher', 'ISSN', 'Widget'])

        next(csv_reader)  # Saltar el encabezado del archivo de entrada, si existe
        for row in csv_reader:
            if len(row) > 0:
                url = row[-1]  # Asumiendo que el URL está en la última columna
                print(f"Scraping {url}")
                data = scrape_url(url)
                csv_writer.writerow([data['Sitio web'], data['Subject Area and category'], data['Publisher'], data['ISSN'], data['Widget']])

if __name__ == '__main__':
    main()
