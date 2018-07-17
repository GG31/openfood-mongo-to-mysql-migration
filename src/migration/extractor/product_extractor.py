from .product_model import Product


class ProductExtractor:
    def __init__(self, category_extractor, country_origin_extractor, country_selling_extractor,
                 brand_extractor, additive_extractor, ingredient_extractor):
        self.category_extractor = category_extractor
        self.country_origin_extractor = country_origin_extractor
        self.country_selling_extractor = country_selling_extractor
        self.brand_extractor = brand_extractor
        self.additive_extractor = additive_extractor
        self.ingredient_extractor = ingredient_extractor

    def extract(self, mongo_product):
        categories = self.category_extractor.extract(mongo_product)
        origin_countries = self.country_origin_extractor.extract(mongo_product)
        selling_countries = self.country_selling_extractor.extract(mongo_product)
        brands = self.brand_extractor.extract(mongo_product)
        additives = self.additive_extractor.extract(mongo_product)
        ingredients = self.ingredient_extractor.extract(mongo_product)
        # TODO create all other fields
        name = mongo_product['product_name'] if 'product_name' in mongo_product else None
        language = mongo_product['lang'] if 'lang' in mongo_product else None
        barcode = mongo_product['code'] if 'code' in mongo_product else None
        product = Product(name=name,
                          language=language,
                          barcode=barcode,
                          category=categories,
                          origin_country=origin_countries,
                          selling_country=selling_countries,
                          brand=brands,
                          additive=additives,
                          ingredient=ingredients
                          )
        return product
