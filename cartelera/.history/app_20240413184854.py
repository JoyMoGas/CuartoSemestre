from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes
from funciones import crea_diccionario_peliculas
from funciones import crea_diccionario_genero
from funciones import crea_diccionario_anios
from funciones import crea_diccionario_alfabeto
import os


archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)
diccionario_anios = crea_diccionario_anios(cartelera)
diccionario_alfabeto = crea_diccionario_alfabeto(cartelera)

@app.route("/")
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas)

@app.route("/generos")
def generos():
    return render_template("generos.html",dicc_generos=diccionario_generos)



@app.route("/anios")
def anio():
    return render_template("anio.html", dicc_anios=diccionario_anios)

@app.route("/alfabetico")
def alfabetico():
    return render_template("alfabetico.html", dicc_alfabetico=diccionario_alfabeto)

@app.route("/genero/<genero>")
def solo_genero(genero):
    if genero in dicc_generos:
        lista_peliculas = dicc_generos[genero]
        return render_template("solo_genero.html", genero=genero, lista_peliculas=lista_peliculas)
    else:
        return render_template("no_existe.html")


@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]  
        print(f"movie={pelicula['titulo']}")  
        return render_template("movie.html",movie=pelicula)
    else:
        return render_template("no_existe.html")
    
if __name__ == "__main__":
    app.run(debug=True)