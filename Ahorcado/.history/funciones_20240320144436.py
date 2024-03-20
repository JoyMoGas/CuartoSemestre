def lee_archivo(archivo:str):
    data = []
    with open(archivo, "r", ebcoding="utf-8") as a:
        data = a.readlines()
    return data

if __name__ == "__main__":
    palabras = lee_archivo("palabras.txt")
    print(palabras)