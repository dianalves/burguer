from infrastructure.repository.burger_repository import BurgerRepository, BurgerPeweeModel, IngredientPeweeModel
from infrastructure.service.db import get_database

def seed_burgers():
    burgers_data = [
        {'name': 'Veg-Ovo', 'image': '/public/images/burger1.jpg', 'ingredients': 'Pão, QueijoVeg, Cebola Roxa, Rucula, Pesto Verde, Pesto de Ovo'},
        {'name': 'Veg-Cogumelo', 'image': '/public/images/burger2.jpg', 'ingredients': 'Pão, QueijoVeg, Cogumelo, Alface, Hamburguer de Beterraba'},
        {'name': 'Veg-Verde', 'image': '/public/images/burger3.jpg', 'ingredients': 'Pão Preto, Mix de Salada, Mix de Legumes'},
        {'name': 'Veg-Aborger', 'image': '/public/images/burger4.jpg', 'ingredients': 'Pão, QueijoVeg, Cebola Roxa, Rucula, Hamburguer de Abobrinha'},
        {'name': 'Veg-Hambacate', 'image': '/public/images/burger5.jpg', 'ingredients': 'Pão, QueijoVeg, Creme de Abacate, Cogumelo, Hamburguer de Berinjela'},
    ]

    return burgers_data

def seed_ingredients():
    ingredients_data = [
        {'name': 'Pão', 'price': 1.50},
        {'name': 'Pão Preto', 'price': 1.50},
        {'name': 'QueijoVeg', 'price': 5.00},
        {'name': 'Cebola Roxa', 'price': 0.50},
        {'name': 'Rucula', 'price': 0.75},
        {'name': 'Pesto Verde', 'price': 5.25},
        {'name': 'Pesto de Ovo', 'price': 5.00},
        {'name': 'Cogumelo', 'price': 4.50},
        {'name': 'Alface', 'price': 0.50},
        {'name': 'Hamburguer de Beterraba', 'price': 13.00},
        {'name': 'Mix de Salada', 'price': 7.00},
        {'name': 'Mix de Legumes', 'price': 7.00},
        {'name': 'Hamburguer de Abobrinha', 'price': 13.00},
        {'name': 'Creme de Abacate', 'price': 3.50},
        {'name': 'Hamburguer de Berinjela', 'price': 13.00},
    ]

    return ingredients_data


if __name__ == "__main__":
    mysql = get_database()
    burger_repository = BurgerRepository(mysql)

    # Seed ingredients
    for ingredient in seed_ingredients():
        IngredientPeweeModel.create(**ingredient)

    # Seed burgers
    for burger in seed_burgers():
        BurgerPeweeModel.create(**burger)