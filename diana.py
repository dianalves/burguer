dados_json = {"name": "X-Burguer"}

price_ingredients = {
        "Alface": 0.4,
        "Bacon": 2,
        "Hamburguer de Carne": 3,
        "Ovo": 0.8,
        "Queijo": 1.5,
    }
available_burguers = {
        "X-BACON": {
            "ingredients": ["Bacon", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-bacon.png",
        },
        "X-BURGUER": {
            "ingredients": ["Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-burger.png",
        },
        "X-EGG": {
            "ingredients": ["Ovo", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-egg.png",
        },
        "X ": {
            "ingredients": ["Ovo", "Bacon", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-egg-bacon.png",
        },
    }

expected = {
        "name": "X-Burger",
        "originalPrice": 4.5,
        "promoPrice": 4.5,
        "promotions": [],
    }

name = dados_json.get('name', '')
choosen_buguer = available_burguers.get(name.upper(), {})
ingredients = choosen_buguer.get('ingredients', [])

soma_ingredients = 0
for ingredient in ingredients:
    soma_ingredients +=  price_ingredients.get(ingredient, 0)
print(f'{soma_ingredients=}')
output = {
    'name': name,
    "originalPrice": soma_ingredients,
    "promoPrice": soma_ingredients,
    "promotions": []
}
print(f'{output=}')
assert output == expected
print('')