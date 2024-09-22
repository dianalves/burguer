from infrastructure.repository.burger_repository import BurgerRepository, BurgerPeweeModel
from infrastructure.service.db import get_database

def seed_burgers():
    burgers_data = [
        {'name': 'X-Bacon', 'image': '/public/images/x-bacon.png', 'ingredients': 'Bacon,Hamburguer de Carne,Queijo'},
        {'name': 'X-Burger', 'image': '/public/images/x-burger.png', 'ingredients': 'Hamburguer de Carne,Queijo'},
        {'name': 'X-Egg', 'image': '/public/images/x-egg.png', 'ingredients': 'Ovo,Hamburguer de Carne,Queijo'},
        {'name': 'X-Egg Bacon', 'image': '/public/images/x-egg-bacon.png', 'ingredients': 'Ovo,Bacon,Hamburguer de Carne,Queijo'},
    ]

    return burgers_data

if __name__ == "__main__":
    mysql = get_database()

    burger_repository = BurgerRepository(mysql)

    for burger in seed_burgers():
        BurgerPeweeModel.create(**burger)