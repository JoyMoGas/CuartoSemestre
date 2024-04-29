from flask import Flask, render_template, request
from funciones import carga_inicio
from funciones import crea_diccionario_alfabeto
from funciones import buscar_revistas_por_titulo
from funciones import crea_diccionario_revistas
from funciones import crea_diccionario_revistas_datos
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
    total_results = len(revistas)  # Total de revistas disponibles
    total_pages = (total_results + per_page - 1) // per_page  # Calcula el total de páginas
    return render_template('index.html', lista=revistas[start:end], page=page, total_pages=total_pages, total_results=total_results)

@app.route("/explorar")
def explorar():
    diccionario_alfabeto = crea_diccionario_alfabeto(revistas)
    return render_template('explorar.html', dicc_alfabeto=diccionario_alfabeto)


@app.route("/explorar/<letra>")
def solo_letra(letra):
    diccionario_alfabeto = crea_diccionario_alfabeto(revistas)
    if letra in diccionario_alfabeto:
        page = request.args.get('page', 1, type=int)
        per_page = 40  # Cantidad de revistas por página
        lista_revistas_por_letra = diccionario_alfabeto[letra]
        total_results = len(lista_revistas_por_letra)  # Total de revistas que comienzan con la letra
        total_pages = (total_results + per_page - 1) // per_page
        start = (page - 1) * per_page
        end = start + per_page
        lista_revistas = lista_revistas_por_letra[start:end]
        return render_template('solo_letra.html', letra=letra, lista_revistas=lista_revistas, dicc_alfabeto=diccionario_alfabeto, page=page, total_pages=total_pages, total_results=total_results)
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
    texto_busqueda = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Cantidad de resultados por página

    if texto_busqueda:
        todos_revistas = buscar_revistas_por_titulo(revistas, texto_busqueda)
        total_pages = (len(todos_revistas) + per_page - 1) // per_page
        start = (page - 1) * per_page
        end = start + per_page
        revistas_encontradas = todos_revistas[start:end]

        return render_template('busqueda.html', revistas=revistas_encontradas, busqueda=texto_busqueda, page=page, total_pages=total_pages, total_results=len(todos_revistas))
    return render_template('index.html')

@app.route('/revista/<titulo>')
def revista(titulo: str):
    revistas_datos = carga_inicio('revista_info.csv')
    diccionario_revistas = crea_diccionario_revistas_datos(revistas_datos)
    if titulo in diccionario_revistas:
        revista = diccionario_revistas[titulo]
        return render_template('revista.html', revista=revista)
    else:
        return render_template("no_existe.html")


if __name__ == "__main__":
    app.run(debug=True)
