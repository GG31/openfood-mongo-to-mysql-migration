import pytest
from unittest.mock import patch, MagicMock
from .migration import Migration

import config

test_config = config.get_config('test')


@pytest.fixture
def mysql_client(request):
    mysql_client_mock = MagicMock()
    mysql_client_mock.create_session = MagicMock()
    mysql_client_mock.commit = MagicMock()
    mysql_client_mock.insert = MagicMock()
    mysql_client_mock.get_or_create.return_value = request.param
    return mysql_client_mock


@pytest.fixture
def mongo_db(request):
    collection = MagicMock()
    collection.find.return_value = request.param
    mongo_db_mock = {'test': collection}
    return mongo_db_mock


@pytest.mark.parametrize('mongo_db, mysql_client', [([], None)], indirect=['mongo_db', 'mysql_client'])
def test_migrate_with_no_product(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()


# TODO tests
