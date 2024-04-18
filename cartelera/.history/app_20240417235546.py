from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes
from funciones import crea_diccionario_peliculas
from funciones import crea_diccionario_genero
from funciones import crea_diccionario_anios
from funciones import crea_diccionario_alfabeto
from funciones import crea_diccionario_pelicula
from funciones import peliculas_cartelera
import unicodedata
import os


archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)
diccionario_anios = crea_diccionario_anios(cartelera)
diccionario_alfabeto = crea_diccionario_alfabeto(cartelera)
diccionario_pelicula=crea_diccionario_pelicula(cartelera)

@app.route("/")
def index():
    global cartelera
    lista_peliculas_cartelera = peliculas_cartelera(cartelera)
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas, dicc_generos=diccionario_generos, lista_movie=lista_peliculas_cartelera)

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
    if genero in diccionario_generos:
        lista_peliculas = diccionario_generos[genero]
        return render_template("solo_genero.html", genero=genero, lista_peliculas=lista_peliculas, dicc_generos=diccionario_generos)
    else:
        return render_template("no_existe.html")



@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]
        generos_pelicula = pelicula.get('titulo', '').split(',')
        generos_pelicula = [unicodedata.normalize('NFKD', genero.strip().upper()).encode('ASCII', 'ignore').decode('utf-8') for genero in generos_pelicula]
        return render_template("movie.html", movie=pelicula, generos_pelicula=generos_pelicula, dicc_generos=diccionario_generos)
    else:
        return render_template("no_existe.html")




    
if __name__ == "__main__":
    app.run(debug=True)