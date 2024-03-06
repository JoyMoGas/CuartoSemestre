import requests
from bs4 import BeautifulSoup

def scrap(URL: str):
    '''OBTIENE PAGINA DESDE INTERNET'''
    pagina = requests.get(URL)
    return pagina

def get_exchange_rate(dom):
    exchange_rates = {}
    for row in dom.find_all('p'):
        title = row.text.strip()
        if title[0] == 'C':
            title = 'Compra'
        else:
            title = 'Venta'
        value = row.find('span')
        value = value.text.strip()
        exchange_rates[title] = value # actualizamos dict
    return exchange_rates

def get_exchange_rate_dict(dom):
    dictionary = {}
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        i = 0
        for col in row.find_all('td'):  
            if i == 0:
                institucion = col.find(class_='small-hide')
                institucion = institucion.text.strip()
                dictionary[institucion] = {}
            elif i == 3:
                compra = col.text.strip()
                dictionary[institucion]['compra'] = float(compra)
            elif i == 4:
                venta = col.text.strip()
                dictionary[institucion]['venta'] = float(venta)
            i += 1    

    return dictionary

def main():
    url="https://bit.ly/dolarInfo"
    pagina = scrap(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    table = soup.find(id='dllsTable')
    d = get_exchange_rate_dict(table)
    
    count = 0
    for key, value in d.items():
        compra = value['compra'] if 'compra' in value else 'N/A'
        venta = value['venta'] if 'venta' in value else 'N/A'
        print(f"{key.upper()} -> Compra {compra} | Venta {venta}", end=' ')
        count += 1
        if count == 1:
            print() 
            count = 0 


if __name__ == "__main__":
    main()