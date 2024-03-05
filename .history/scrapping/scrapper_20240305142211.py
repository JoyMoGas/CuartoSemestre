import requests
from bs4 import BeautifulSoup

def scrap(URL: str):
    '''OBTIENE PAGINA DESDE INTERNET'''
    pagina = requests.get(URL)
    return pagina

def get_exchange_rate(dom):
    exchange_rates = {}
    for row in dom.find_all('p'):
       # print(f"{row}")
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
    #result = soup.find(class_="dllsTable")
    #ex = get_table_element(result)
    table = soup-find(id='dllsTable')
    d = get_table_element(table)

def get_table_element(dom):
    dictionary = {}
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        for col in row.find_all('td'):
            print(col)
        assert 1== 0
        


if __name__ == "__main__":
    main()