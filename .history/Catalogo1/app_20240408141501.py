from flask import Flask ,render_template, requests
from funciones import carga_csv
import os

archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)

@app.route('/')
def index():
    return render_template("index.html")