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

def main():
    url="https://bit.ly/dolarInfo"
    pagina = scrap(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    table = soup.find(id='dllsTable')
    d = get_exchange_rate_dict(table)
    

def get_exchange_rate_dict(dom):
    dictionary = {}
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        i = 0
        for col in row.find_all('td'):  
            if i == 0:
                institucion = col.find(class_='small-hide')
                if institucion is not None:
                    institucion = institucion.text.strip()
                    print(institucion)
            if i == 3:
                compra = col.find(class_='xTimes')
                if compra is not None:
                    compra = compra.text.strip()
                    compra = float(compra)
                    print(compra)
            i += 1    
    return ""

if __name__ == "__main__":
    main()