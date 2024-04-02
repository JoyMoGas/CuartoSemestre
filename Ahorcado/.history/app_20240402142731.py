from flask import Flask, render_template, request
from os import path
from funciones import lee_archivo, palabra_a_diccionario
import random 
app = Flask(__name__)

palabras = lee_archivo("palabras.txt")
palabra = random.choice(palabras)
lista_dict = palabra_a_diccionario(palabra)
conteo = 0
lista_dict 
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras = [ x for x in abc]
@app.route('/', methods=['GET','POST'])
def index():
    global conteo
    global lista_dict
    global abc
    if request.method == 'GET':
        print(app.url_map)      
        image = f"/static/images/monito-{conteo}.png"
        string_abc = "".join(letras)
        lista_letras = [ {'letra':x, 'id_letra':x} for x in string_abc]
        listado = [(d['letra'],d['id_letra']) for d in lista_letras]
        return render_template("index.html",
                               imagen=image,
                               lista_abc=listado,
                               abcedario=string_abc,
                               lista_pal=lista_dict)
    if request.method == 'POST':
        valor = request.form['valor']
        valor = valor.lower()
        existe = False
        print(lista_dict)
        for diccionario in lista_dict:
            if valor in diccionario:
                diccionario[valor] = valor
                existe = True
        if existe == False:
            conteo +=1

            letras.remove(valor)
        image = f"/static/images/monito-{conteo}.png"
        string_abc = "".join(letras)
        lista_letras = [ {'letra':x, 'id_letra':x} for x in string_abc]
        listado = [(d['letra'],d['id_letra']) for d in lista_letras]
        return render_template("index.html",
                               imagen=image,
                               abcedario=string_abc,
                               lista_abc=listado,
                               lista_pal=lista_dict)

    
if __name__ == "__main__":
    app.run(debug=True)