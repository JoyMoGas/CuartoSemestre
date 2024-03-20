from flask import Flask, render_template, request
from os import path

app = Flask(__name__)

conteo = 0
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(app.url_map)
        image = f"/static/images/monito-{conteo}.png"
        letras = [{'letra':x, 'id_letra':x}for x in abc]
        listado = [(d['letra'], d['id_letra']) for d in letras]
        return render_template('index.html', imagen=image, abcedario=abc, lista_abc=listado)