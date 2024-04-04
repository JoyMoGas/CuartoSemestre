import csv

def carga_csv(nombre_archivo: str) -> list:
    '''
    Carga archivo csv y regresa una lista
    '''
    lista = []
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        lista = csv.DictReader(archivo)

    return lista