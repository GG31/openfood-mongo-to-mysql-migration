from .additive_model import Additive


class AdditiveExtractor:
    def __init__(self, mysql_client):
        self.mysql_client = mysql_client

    def extract(self, mongo_product):
        additives = []
        if 'additives_tags' in mongo_product:
            for additive_tag in mongo_product['additives_tags']:
                additive = self.mysql_client.get_or_create(Additive, tag=additive_tag)
                additives.append(additive)
        return additives
