import csv
from datetime import datetime

def carga_csv(nombre_archivo: str) -> list:
    '''
    Carga archivo csv y regresa una lista
    '''
    lista = []
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

def peliculas_mas_recientes(lista_peliculas: str) -> list:
    '''Regresa las películas de más reciente estreno'''
    lista = []
    hoy = datetime.now()
    for pelicula in lista_peliculas:
        estreno = pelicula['fecha_estreno']
        estreno = datetime.strptime(estreno, "%Y-%m-%d")
        diferencia = hoy - estreno
        pelicula['dias_desde_estreno'] = diferencia.days()
        lista_peliculas.sort(key=lambda x: x['dias_desde_estreno'])
        for i, pelicula in enumerate(lista_peliculas):
            if i<5:
                lista.append(pelicula)
            return lista

if __name__ == "__main__":
    lista = carga_csv("cartelera_2024.csv")
    print(lista)