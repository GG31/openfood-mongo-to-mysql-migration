
class Helper:
    def __init__(self, mysql_client):
        self.mysql_client = mysql_client

    def extract_names_and_tags(self, mongo_product, model_name, tags_field, names_fields):
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
