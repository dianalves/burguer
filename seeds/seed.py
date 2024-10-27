from infrastructure.repository.burger_repository import BurgerRepository, BurgerPeweeModel
from infrastructure.service.db import get_database

def seed_burgers():
    burgers_data = [
        {'name': 'Veg-Ovo', 'image': '/public/images/burger1.jpg', 'ingredients': 'Pão, QueijoVeg, Cebola Roxa, Rucula, Pesto Verde, Pesto de Ovo'},
        {'name': 'Veg-Cogumelo', 'image': '/public/images/burger2.jpg', 'ingredients': 'Pão, QueijoVeg, Cogumelo, Alface, Hamburguer de Beterraba'},
        {'name': 'Veg-Verde', 'image': '/public/images/burger3.jpg', 'ingredients': 'Pão Preto, Mix de salada, Mix de legumes'},
        {'name': 'Veg-Aborger', 'image': '/public/images/burger4.jpg', 'ingredients': 'Pão, QueijoVeg, Cebola Roxa, Rucula, Hamburguer de Abobrinha'},
        {'name': 'Veg-Hambacate', 'image': '/public/images/burger5.jpg', 'ingredients': 'Pão, QueijoVeg, Creme de Abacate, Cogumelo, Hamburguer de Berinjela'},
    ]

    return burgers_data

if __name__ == "__main__":
    mysql = get_database()

    burger_repository = BurgerRepository(mysql)

    for burger in seed_burgers():
        BurgerPeweeModel.create(**burger)