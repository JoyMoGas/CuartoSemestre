from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explorar')
def explorar():
    return render_template('index.html')

@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/acerca-de')
def acerca_de():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
