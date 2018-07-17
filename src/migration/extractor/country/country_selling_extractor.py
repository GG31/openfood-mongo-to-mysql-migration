from .country_model import Country


class CountrySellingExtractor:
    def __init__(self, helper):
        self.helper = helper

    def extract(self, mongo_product):
        selling_countries = self.helper.extract_names_and_tags(mongo_product, Country, 'countries_tags', 'countries')
        return selling_countries
