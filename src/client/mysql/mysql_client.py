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

    def insert(self, item):
        self.mysql_session.add(item)
        self.nb_item += 1
        if self.nb_item == self.bulk_limit:
            self.mysql_session.commit()
            self.nb_item = 0


