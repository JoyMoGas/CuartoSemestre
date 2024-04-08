from flask import Flask ,render_template, requests
from funciones import carga_csv
import os

archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generos')
def generos():
    return render_template("generos.html")


@app.route('/anio')
def anio():
    return render_template("anio.html")


@app.route('/alfabetico')
def alfabetico():
    return render_template("alfabetico.html")


@app.route('/pelicula')
def pelicula():
    return render_template("pelicula.html")