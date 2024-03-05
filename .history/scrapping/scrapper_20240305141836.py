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
    result = soup.find(class_="dllsTable")
    ex = get_table_element(result)
    print(ex)


def get_table_element(dom):
    table_data = []
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        row_data = {}
        for i, col in enumerate(row.find_all('td')):
            row_data[i] = col.text
        table_data.append(row_data)
    return table_data


if __name__ == "__main__":
    main()