import csv

def carga_csv(nombre_archivo: str) -> list:
    '''
    Carga archivo csv y regresa una lista
    '''
    lista = []
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

if __name__ == "__main__":
    lista = carga_csv("codigos/cartelera_2024.csv")
    print(lista)