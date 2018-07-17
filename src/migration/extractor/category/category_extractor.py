from .category_model import Category


class CategoryExtractor:
    def __init__(self, helper):
        self.helper = helper

    def extract(self, mongo_product):
        categories = self.helper.extract_names_and_tags(mongo_product, Category, 'categories_tags', 'categories')
        return categories
