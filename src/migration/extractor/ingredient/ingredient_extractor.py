from .ingredient_model import Ingredient


class IngredientExtractor:
    def __init__(self, mysql_client):
        self.mysql_client = mysql_client

    def extract(self, mongo_product):
        ingredients = []
        # TODO check length, lower case, well written
        print(mongo_product)
        if 'ingredients' in mongo_product:
            for ingredient_item in mongo_product['ingredients']:
                print(ingredient_item['id'])
                print(ingredient_item['text'])
                if len(ingredient_item['id']) <= 100 and len(ingredient_item['id']) <= 100:
                    ingredient = self.mysql_client.get_or_create(
                        Ingredient,
                        tag=ingredient_item['id'].lower(),
                        name=ingredient_item['text'].lower()
                    )
                    ingredients.append(ingredient)
        return ingredients
