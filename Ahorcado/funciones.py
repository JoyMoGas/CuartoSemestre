def lee_archivo(archivo:str):
    palabras = []
    with open(archivo, "r", encoding="utf-8") as a:
        data = a.readlines()
        for palabra in data:
            palabra = palabra.strip('\n')
            palabras.append(palabra)
    return data

if __name__ == "__main__":
    palabras = lee_archivo("palabras.txt")
    print(palabras)