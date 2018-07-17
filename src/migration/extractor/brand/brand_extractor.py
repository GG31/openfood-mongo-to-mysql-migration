from .brand_model import Brand


class BrandExtractor:
    def __init__(self, helper):
        self.helper = helper

    def extract(self, mongo_product):
        brands = self.helper.extract_names_and_tags(mongo_product, Brand, 'brands_tags', 'brands')
        return brands
