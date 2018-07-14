from .models import Product, Category


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
            product = self.create_product(mongo_product)
            print(product)
            self.mysql_client.insert(product)
        self.mysql_client.commit()
        self.logger.info('Migration finished')

    def create_product(self, mongo_product):
        categories = self.create_categories(mongo_product)
        # TODO create all other fields
        name = mongo_product['product_name'] if 'product_name' in mongo_product else None
        language = mongo_product['lang'] if 'lang' in mongo_product else None
        barcode = mongo_product['code'] if 'code' in mongo_product else None
        product = Product(name=name, language=language, barcode=barcode, category=categories)
        return product

    def create_categories(self, mongo_product):
        categories = []
        if 'categories_tags' in mongo_product and 'categories' in mongo_product:
            for (tag, name) in zip(mongo_product['categories_tags'], mongo_product['categories'].split(',')):
                category = self.mysql_client.get_or_create(Category, tag=tag, name=name)
                categories.append(category)
        return categories
