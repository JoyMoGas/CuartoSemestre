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
    
    best_option = None
    best_compra = float('inf')
    best_venta = float('inf')
    
    for key, value in d.items():
        compra = value['compra'] if 'compra' in value else float('inf')
        venta = value['venta'] if 'venta' in value else float('inf')
        if compra < best_compra and venta < best_venta:
            best_option = key
            best_compra = compra
            best_venta = venta
        print(f"{key.upper()} -> Compra {compra if compra != float('inf') else 'N/A'} | Venta {venta if venta != float('inf') else 'N/A'}")
    
    if best_option is not None:
        print("----------------------------------")
        print(f"LA MEJOR OPCION ES: {best_option.upper()} -> Compra {best_compra} | Venta {best_venta}")


if __name__ == "__main__":
    main()