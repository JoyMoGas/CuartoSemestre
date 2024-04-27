from flask import Flask, render_template, request
from funciones import carga_inicio
from funciones import crea_diccionario_alfabeto
from funciones import buscar_revistas_por_titulo
import unicodedata

app = Flask(__name__)



# Carga de revistas desde CSV o generación de datos de prueba
try:
    revistas = carga_inicio('revistas.csv')
except FileNotFoundError:
    # Generar datos de prueba con todos los campos necesarios
    revistas = [
        {
            'Titulo': f'Revista {i}',
            'Type': 'Tipo ' + ('A' if i % 2 == 0 else 'B'),
            'SJR (Cuartil)': 'Q' + str(i % 4 + 1),
            'H_Index': i % 100
        } for i in range(29166)
    ]

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 50
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(revistas) + per_page - 1) // per_page  # Calcula el total de páginas
    return render_template('index.html', lista=revistas[start:end], page=page, total_pages=total_pages)

@app.route("/explorar")
def explorar():
    diccionario_alfabeto = crea_diccionario_alfabeto(revistas)
    return render_template('explorar.html', dicc_alfabeto=diccionario_alfabeto)


@app.route("/explorar/<letra>")
def solo_letra(letra):
    diccionario_alfabeto = crea_diccionario_alfabeto(revistas)
    if letra in diccionario_alfabeto:
        page = request.args.get('page', 1, type=int)
        per_page = 40  # Cambia esto según cuántas revistas quieres mostrar por página
        start = (page - 1) * per_page
        end = start + per_page
        lista_revistas = diccionario_alfabeto[letra][start:end]
        total_pages = (len(diccionario_alfabeto[letra]) + per_page - 1) // per_page
        return render_template('solo_letra.html', letra=letra, lista_revistas=lista_revistas, dicc_alfabeto=diccionario_alfabeto, page=page, total_pages=total_pages)
    else:
        return render_template('no_existe.html')


@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/acerca-de')
def acerca_de():
    return render_template('about.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    texto_busqueda = request.args.get('search', '')  # Obtiene la palabra de búsqueda del formulario
    if texto_busqueda:
        revistas_encontradas = buscar_revistas_por_titulo(revistas, texto_busqueda)
        return render_template('revista.html', revistas=revistas_encontradas, busqueda=texto_busqueda)
    return render_template('index.html')  # Redirige a la página principal si no hay búsqueda


if __name__ == "__main__":
    app.run(debug=True)
