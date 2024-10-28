from peewee import Model, CharField, DecimalField


class BurgerPeweeModel(Model):
    name = CharField()
    image = CharField()
    ingredients = CharField()


    class Meta:
        table_name = 'burger'
        database = None

class IngredientPeweeModel(Model):
    name = CharField(unique=True)
    price = DecimalField()

    class Meta:
        table_name = 'ingredient'
        database = None

class BurgerRepository():
    def __init__(self, db):
        BurgerPeweeModel._meta.database = db
        IngredientPeweeModel._meta.database = db
        self.db = db

        with self.db.connection_context():
            self.db.create_tables([BurgerPeweeModel, IngredientPeweeModel])

    def list_all_burgers(self) -> list[BurgerPeweeModel]:
        with self.db.connection_context():
            burgers = list(BurgerPeweeModel.select())
        return burgers