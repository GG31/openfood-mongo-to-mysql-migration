from .country_model import Country


class CountryOriginExtractor:
    def __init__(self, helper):
        self.helper = helper

    def extract(self, mongo_product):
        origins = self.helper.extract_names_and_tags(mongo_product, Country, 'origins_tags', 'origins')
        return origins
