import csv
import unicodedata

def carga_inicio(nombre_archivo: str) -> list:
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            lista = list(csv.DictReader(archivo))
        return lista
    except Exception as e:
        print(f"Error al abrir o leer el archivo: {e}")
        return []  # Retornamos una lista vacía si hay un error

def revistas_index(lista_revistas: list) -> list:
    # Suponiendo que quieres ordenar las revistas por el campo 'Titulo'
    lista_ordenada = sorted(lista_revistas, key=lambda x: x['Titulo'], reverse=False)
    print(lista_ordenada)
    return lista_ordenada

def crea_diccionario_alfabeto(lista_revistas: list) -> dict:
    d = {}
    for revista in lista_revistas:
        titulo = revista["Titulo"]
        # Normalizar y convertir a mayúsculas la primera letra
        primera_letra = unicodedata.normalize('NFD', titulo[0]).encode('ascii', 'ignore').decode('utf-8').upper()
        
        # Agregar revista al diccionario bajo la clave de su primera letra
        if primera_letra in d:
            d[primera_letra].append(revista)
        else:
            d[primera_letra] = [revista]

    # Ordenar el diccionario por las claves (letras)
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d

# En funciones.py
def buscar_revistas_por_titulo(revistas, texto_busqueda):
    texto_busqueda = texto_busqueda.lower()
    return [revista for revista in revistas if texto_busqueda in revista['Titulo'].lower()]

def crea_diccionario_revistas(lista_revistas:list)->dict:
    ''' Crea diccionario de peliculas a partir de 
        la lista de peliculas
        {"id_pelicula" ={diccionario_pelicula}}
    '''
    d = {}
    for revista in lista_revistas:
        key = revista["Titulo"]
        d[key] = revista # key,value
    return d

def crea_diccionario_revistas_datos(lista_revistas):
    d = {}
    for revista in lista_revistas:
        key = revista["TITLE"]
        d[key] = revista
    return d

def carga_datos_revistas_info(lista_revistas: str) -> dict:
    ''' Crea diccionario de peliculas a partir de 
        la lista de peliculas
        {"id_pelicula" ={diccionario_pelicula}}
    '''
    d = {}
    for revista in lista_revistas:
        key = revista["URL"]
        d[key] = revista # key,value
    return d



if __name__ == "__main__":
    lista_de_revistas = carga_inicio('revistas.csv')
    if lista_de_revistas:
        lista_ordenada = revistas_index(lista_de_revistas)
    else:
        print("No se cargaron datos desde el archivo CSV.")
