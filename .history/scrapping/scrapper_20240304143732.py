import requests
from bs4 import BeautifulSoup

def scrap(URL: str):
    '''OBTIENE PAGINA DESDE INTERNET'''
    pagina = requests.get(URL)
    return pagina

def main():
    url="https://bit.ly/dolarInfo"
    pagina = scrap(url)
    print(pagina.content)

if __name__ == "__main__":
    main()