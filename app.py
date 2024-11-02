from typing import Optional

from flask import Flask, render_template, request, jsonify, make_response
# from models.mysql import execute as service
from uuid import uuid4 as generate_session_id

from infrastructure.repository.burger_repository import BurgerRepository, IngredientPeweeModel
from infrastructure.service.db import get_database
from tests.utils.stubs import db_results as db

app = Flask(__name__, template_folder="template", static_folder="public")
burger_repository: Optional[BurgerRepository] = BurgerRepository(get_database())

session = {
    #session_id: {'carrinho': []}
}

# ---------------- Pages -----------------------
@app.route("/")
def home():
    session_id = request.cookies.get('session_id', str(generate_session_id()))

    resp = make_response(render_template("jinja_main.html", title="Binho Burguer"))
    resp.set_cookie('session_id', session_id)

    return resp


@app.route("/carrinho")
def carrinho():
    return render_template("jinja_carrinho.html")


@app.route("/diy")
def diy():
    return render_template("jinja_diy.html")


# ---------------- APIs ------------------------


@app.route("/api/v1.0/burgers")
def burguers():
    # records = db("select * from burguer_page;")
    records = burger_repository.list_all_burgers()

    # for burger in records:
    #     print(burger.image)

    output = {}

    for burger in records:
        name = burger.name
        image = burger.image
        ingredients = burger.ingredients.split(",")

        output[name] = {"ingredients": ingredients, "image": image}

    # for linha in records:
    #     name = linha["name"]
    #     image = linha["image"]
    #     ingredients = linha["ingredients"].split(",")
    #
    #     output[name] = {"ingredients": ingredients, "image": image}

    return output


@app.route("/api/v1.0/ingredients")
def ingredients():
    # Obtém todos os ingredientes usando o modelo
    records = IngredientPeweeModel.select()

    resp = {}

    for ingredient in records:
        name = ingredient.name
        price = ingredient.price

        resp[name] = price

    return resp

@app.route("/api/v1.0/calculate", methods=["POST"])
def calculate():
    dados_json = request.get_json()

    # Obter todos os ingredientes e seus preços
    price_ingredients = {ingredient.name: ingredient.price for ingredient in IngredientPeweeModel.select()}
    available_burgers = burguers()  # Chama a função para obter burgers

    name = dados_json.get('name', '')
    choosen_burger = available_burgers.get(name, {})
    current_ingredients = choosen_burger.get('ingredients', {})
    current_ingredients = [ingredient.strip() for ingredient in current_ingredients]

    print(current_ingredients)

    soma_ingredients = 0
    for ingredient in current_ingredients:
        price = price_ingredients.get(ingredient, 0)
        soma_ingredients += price  # Adiciona o preço do ingrediente à soma total

    print(f'{soma_ingredients=}')
    output = {
        'name': name,
        "originalPrice": f"{soma_ingredients:.2f}",
        "promoPrice": f"{soma_ingredients:.2f}",
        "promotions": []
    }

    return jsonify(output)

@app.route("/api/v1.0/carrinho", methods=["POST", "GET", "DELETE"])
def session_carrinho():
    session_id = request.cookies.get('session_id', None)

    user_session = session.get(session_id, {})
    carrinho = user_session.get('carrinho', [])

    if request.method == 'GET':
        return jsonify({'carrinho': carrinho}), 200

    elif request.method == 'DELETE':
        item_to_remove = request.get_json().get('name', None)
        itens_with_the_same_name = [idx for idx, item in enumerate(carrinho) if item['name'] == item_to_remove]

        if len(itens_with_the_same_name):
            index = itens_with_the_same_name[0]

            carrinho.pop(index)

            return jsonify({'carrinho': carrinho}), 200
        return jsonify({}), 404

    elif request.method == 'POST':
        new_item = request.get_json()

        carrinho.append(new_item)
        user_session['carrinho'] = carrinho
        session[session_id] = user_session

        return jsonify({}), 201

    return {}

if __name__ == "__main__":
    mysql = get_database()

    burger_repository = BurgerRepository(mysql)

    app.run(host='0.0.0.0', debug=True)
