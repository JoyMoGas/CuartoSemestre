import requests
from bs4 import BeautifulSoup

def scrap(URL: str):
    '''OBTIENE PAGINA DESDE INTERNET'''
    pagina = requests.get(URL)
    return pagina

def get_exchange_rate(dom):
    exchange_rates = []
    for row in dom.find_all('p'):
        print(f"{row}")
    return exchange_rates

def main():
    url="https://bit.ly/dolarInfo"
    pagina = scrap(url)
    result = BeautifulSoup(pagina.content, "html.parser")
    ex = get_exchange_rate(result)
    print(pagina.content)

if __name__ == "__main__":
    main()