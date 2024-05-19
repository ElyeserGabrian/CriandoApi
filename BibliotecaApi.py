from flask import Flask, jsonify, render_template

app = Flask(__name__)

livros = []

nomes = ["1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "Moby-Dick", "Ate o verao Terminar"]
autores = ["George Orwell", "Harper Lee", "Jane Austen", "F. Scott Fitzgerald", "Herman Melville", "Colleen Hover"]

for i in range(len(nomes)):
    livro = {'id': i+1, 'Nome': nomes[i], 'Autores': autores[i] }
    livros.append(livro)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/livros')
def lista_livro():
    return livros

@app.route('/livros/<int:id>')
def livro_esp(id):
    for book in livros:
        if book.get('id') == id:
            return jsonify(book)

app.run(port=5000, host='localhost', debug=True)
