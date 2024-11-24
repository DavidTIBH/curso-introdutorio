from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Abrir terminal com flask shell. Após criar a classe, usar os seguintes códigos no terminal: db.create_all(), esse código vai criar as tabelas.
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    # db.session.commit, após criar tudo, esse código faz a atualização, faz a modificação, após isso devemos usar exit() para sair do terminal.

# Esse add adiciona novos produtos
@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201  # Retorna sucesso com código 201 (Created)
    
    return jsonify({"message": "Missing required fields: 'name' and 'price'"}), 400  # Retorna erro se campos obrigatórios estiverem ausentes

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar.
@app.route('/')
def hello_world():
    return 'Olá, seja bem-vindo!'

if __name__ == "__main__":
    app.run(debug=True)