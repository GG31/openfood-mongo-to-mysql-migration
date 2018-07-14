from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class MySqlClient:
    def __init__(self, config):
        self.config = config
        self.mysql_session = None
        self.bulk_limit = 1000
        self.nb_item = 0

    def create_session(self, url):
        mysql_engine = create_engine(url)
        self.mysql_session = Session(mysql_engine)
        return self.mysql_session

    def insert(self, item):
        self.mysql_session.add(item)
        self.nb_item += 1
        # if self.nb_item == self.bulk_limit:
        self.commit()

    def get_or_create(self, model, **kwargs):
        query = self.mysql_session.query(model).filter_by(**kwargs)
        if query.count() == 0:
            item = model(**kwargs)
        else:
            item = query.one()
        return item

    def merge(self, item):
        self.mysql_session.merge(item)
        self.nb_item += 1
        # if self.nb_item == self.bulk_limit:
        self.commit()

    def commit(self):
        self.mysql_session.commit()
        self.nb_item = 0

