from pytest_stub.toolbox import stub_global

def db_results(sql):
    if sql == "select name, price from ingredient;":
        return [
            {"name": "Alface", "price": 0.4},
            {"name": "Bacon", "price": 2.0},
            {"name": "Hamburguer de Carne", "price": 3.0},
            {"name": "Ovo", "price": 0.8},
            {"name": "Queijo", "price": 1.5},
        ]
    elif sql == "select * from burguer_page;":
        return [
            {
                "ingredients": "Bacon,Hamburguer de Carne,Queijo",
                "name": "X-BACON",
                "image": "/public/images/x-bacon.png",
            },
            {
                "ingredients": "Hamburguer de Carne,Queijo",
                "name": "X-BURGUER",
                "image": "/public/images/x-burger.png",
            },
            {
                "ingredients": "Ovo,Hamburguer de Carne,Queijo",
                "name": "X-EGG",
                "image": "/public/images/x-egg.png",
            },
            {
                "ingredients": "Ovo,Bacon,Hamburguer de Carne,Queijo",
                "name": "X-EGG BACON",
                "image": "/public/images/x-egg-bacon.png",
            },
        ]
    else:
        return []


stub_global({
    "models.mysql.execute": db_results,
})