from flask import Flask, render_template
from models.python import execute as db

app = Flask(__name__, template_folder='template', static_folder='public')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/diy')
def diy():
    return render_template('diy.html')

@app.route('/test')
def test():
    records = db("""select burguer.name, group_concat(ingredient.name) as ingredients
                    from burguer 
                    join BurguerIngredients on burguer.id = BurguerIngredients.burguer_id
                    join ingredient on BurguerIngredients.ingredient_id = ingredient.id
                    group by burguer.name;""")

    return {'results' : records}

if __name__ == '__main__':
    app.run(debug=True)