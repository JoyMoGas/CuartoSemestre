import csv
from datetime import datetime

def carga_csv(nombre_archivo:str)->list:
    '''
    Carga archivo csv y regresa una lista 
    '''
    lista = []
    with open(nombre_archivo,'r',encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

def peliculas_mas_recientes(lista_peliculas:list)->list:
    '''Regresa las películas de más reciente estreno'''
    listap = []
    hoy = datetime.now()
    for pelicula in lista_peliculas:
        #print(pelicula['titulo']," - ",pelicula['fecha_estreno'])
        estreno = pelicula['fecha_estreno']
        estreno = datetime.strptime(estreno,"%Y/%m/%d")
        diferencia = hoy - estreno
        pelicula['dias_desde_estreno'] = diferencia.days
    lista_sorted = sorted(lista_peliculas, key=lambda x: x['dias_desde_estreno'],reverse=False)
    listap = lista_sorted[:5]
    return listap


if __name__ == "__main__":
    lista =carga_csv("cartelera_2024.csv")
    #print(lista)
    print("..........")
    lista5 = peliculas_mas_recientes(lista)
    for pelicula in lista5:
        print(f"{pelicula['titulo']} - {pelicula['fecha_estreno']} {pelicula['dias_desde_estreno']}")
