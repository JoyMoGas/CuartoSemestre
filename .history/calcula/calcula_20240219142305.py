'''
Calcula diferentes tipos de funciones 
estadísticas en una lista de números
'''

def suma(lista: list) -> float:
    return sum(lista)

def promedio(lista: list) -> float:
    '''
    Calcula el promedio de la lista
    Primero sumamos los elementos de la lista
    Segundo, dividimos sobre el total de elementos
    '''
    return suma(lista)/len(lista)

def main(lista: list):
    print(f"Suma: {suma(lista)}")
    print(f"Promedio: {promedio(lista)}")

if __name__ == "__main__":
    listado = [5,6,7,8]
    main(listado)