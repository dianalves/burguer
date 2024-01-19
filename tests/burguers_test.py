from app import burguers


def test_burguers_api():
    expected = {
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
        "X-EGG BACON": {
            "ingredients": ["Ovo", "Bacon", "Hamburguer de Carne", "Queijo"],
            "image": "/public/images/x-egg-bacon.png",
        },
    }

    output = burguers()

    print(output)

    assert output == expected
