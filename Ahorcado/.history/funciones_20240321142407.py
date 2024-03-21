import random

def lee_archivo(archivo:str):
    palabras = []
    with open(archivo, "r", encoding="utf-8") as a:
        data = a.readlines()
        for palabra in data:
            palabra = palabra.strip('\n')
            palabras.append(palabra)
    return palabras

def palabra_a_diciconario(palabra:str)->list:
    '''Convierte palabra en un diccionario de letras'''
    lista = [ {letra: "_"} for letra in palabra ]
    return lista



if __name__ == "__main__":
    palabras = lee_archivo("palabras.txt")
    print(palabras)
    palabra = random.choice(palabras)
    dp = palabra_a_diciconario(palabra)
    print(dp)
    print(", ".join(map(str, dp)))
