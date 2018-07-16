import pytest
from unittest.mock import patch, MagicMock, call
from .migration import Migration
from .models import Category, Product

import config

test_config = config.get_config('test')


def mysql_client_side_effect(model_name, tag, name):
    object_mock = model_name(tag=tag, name=name)
    return object_mock


@pytest.fixture
def mysql_client():
    mysql_client_mock = MagicMock()
    mysql_client_mock.create_session = MagicMock()
    mysql_client_mock.commit = MagicMock()
    mysql_client_mock.insert = MagicMock()
    mysql_client_mock.get_or_create = MagicMock(side_effect=mysql_client_side_effect)
    return mysql_client_mock


@pytest.fixture
def mongo_db(request):
    collection = MagicMock()
    collection.find.return_value = request.param
    mongo_db_mock = {'test': collection}
    return mongo_db_mock


@pytest.mark.parametrize('mongo_db', [([])], indirect=['mongo_db'])
def test_migrate_with_no_product(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()


products = [{
    'product_name': 'test1',
    'code': 'code_test',
    'lang': 'fr',
    'categories': 'cat1,cat2',
    'categories_tags': ['cat1', 'cat2']
}]
@pytest.mark.parametrize('mongo_db', [(products)], indirect=['mongo_db'])
def test_migrate_with_product_categories(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()
    call1 = call(Category, tag='cat1', name='cat1')
    call2 = call(Category, tag='cat2', name='cat2')
    mysql_client.get_or_create.assert_has_calls([call1, call2])
    mysql_client.commit.assert_called_once()
    # mysql_client.insert.assert_called_once_with(Product(name='test1', language='fr', barcode='code_test', category=[Category(tag='cat1', name='cat1'), Category(tag='cat2', name='cat2')]))
# TODO tests
