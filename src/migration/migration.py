from .product import Product


class Migration:
    def __init__(self, config, logger, mongo_db, mysql_client):
        self.config = config
        self.logger = logger.get_logger(__name__)
        self.mongo_db = mongo_db
        self.mysql_client = mysql_client

    def migrate(self):
        collection = self.mongo_db[self.config['mongo']['collection']]
        cursor = collection.find()

        self.mysql_client.create_session(self.config['mysql']['url'])
        for mongo_product in cursor:
            product = Product(mongo_product)
            self.mysql_client.insert(product)
            print(product)
        self.logger.info('Migration finished')
