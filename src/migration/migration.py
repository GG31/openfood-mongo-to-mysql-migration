from .models import Product, Category, Country, Brand, Additive


class Migration:
    def __init__(self, config, logger, mongo_db, mysql_client):
        self.config = config
        self.logger = logger.get_logger(__name__)
        self.mongo_db = mongo_db
        self.mysql_client = mysql_client
        self.session = None

    def migrate(self):
        collection = self.mongo_db[self.config['mongo']['collection']]
        cursor = collection.find()

        self.session = self.mysql_client.create_session(self.config['mysql']['url'])
        for mongo_product in cursor:
            product = self.__create_product(mongo_product)
            self.logger.info('inserting ' + str(product))
            self.mysql_client.insert(product)
        self.mysql_client.commit()
        self.logger.info('Migration finished')

    def __create_product(self, mongo_product):
        categories = self.__create_categories(mongo_product)
        origin_countries = self.__create_origin_countries(mongo_product)
        selling_countries = self.__create_selling_countries(mongo_product)
        brands = self.__create_brands(mongo_product)
        additives = self.__create_additives(mongo_product)
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
                          additive=additives
                          )
        return product

    def __create_categories(self, mongo_product):
        origins = self.__extract_names_and_tags(mongo_product, Category, 'categories_tags', 'categories')
        return origins

    def __create_origin_countries(self, mongo_product):
        origins = self.__extract_names_and_tags(mongo_product, Country, 'origins_tags', 'origins')
        return origins

    def __create_selling_countries(self, mongo_product):
        selling_countries = self.__extract_names_and_tags(mongo_product, Country, 'countries_tags', 'countries')
        return selling_countries

    def __create_brands(self, mongo_product):
        brands = self.__extract_names_and_tags(mongo_product, Brand, 'brands_tags', 'brands')
        return brands

    def __create_additives(self, mongo_product):
        additives = []
        if 'additives_tags' in mongo_product:
            for additive_tag in mongo_product['additives_tags']:
                additive = self.mysql_client.get_or_create(Additive, tag=additive_tag)
                additives.append(additive)
        return additives

    def __extract_names_and_tags(self, mongo_product, model_name, tags_field, names_fields):
        if names_fields in mongo_product and tags_field in mongo_product:
            items = self.__iterate_and_get_or_create(model_name, mongo_product[tags_field], mongo_product[names_fields].split(','))
            return items
        return []

    def __iterate_and_get_or_create(self, model_name, tags, names):
        items = []
        for (tag, name) in zip(tags, names):
            item = self.mysql_client.get_or_create(model_name, tag=tag, name=name)
            items.append(item)
        return items
