

class Migration:
    def __init__(self, config, logger, mongo_db, mysql_client, product_extractor):
        self.config = config
        self.logger = logger.get_logger(__name__)
        self.product_extractor = product_extractor
        self.mongo_db = mongo_db
        self.mysql_client = mysql_client
        self.session = None

    def migrate(self):
        collection = self.mongo_db[self.config['mongo']['collection']]
        cursor = collection.find()

        self.session = self.mysql_client.create_session(self.config['mysql']['url'])
        for mongo_product in cursor:
            product = self.product_extractor.extract(mongo_product)
            self.logger.info('inserting ' + str(product))
            self.mysql_client.insert(product)
        self.mysql_client.commit()
        self.logger.info('Migration finished')
