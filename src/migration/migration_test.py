import pytest
from unittest.mock import patch, MagicMock, call
from .migration import Migration
from .models import Category, Country, Brand, Additive

import config

test_config = config.get_config('test')


def mysql_client_side_effect(model_name, **kwargs):
    object_mock = model_name(**kwargs)
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


products = [{
    'product_name': 'test1',
    'code': 'code_test',
    'lang': 'fr',
    'origins': 'origin1,origin2',
    'origins_tags': ['or1', 'or2']
}]
@pytest.mark.parametrize('mongo_db', [(products)], indirect=['mongo_db'])
def test_migrate_with_product_country_origin(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()
    call1 = call(Country, tag='or1', name='origin1')
    call2 = call(Country, tag='or2', name='origin2')
    mysql_client.get_or_create.assert_has_calls([call1, call2])
    mysql_client.commit.assert_called_once()


products = [{
    'product_name': 'test1',
    'code': 'code_test',
    'lang': 'fr',
    'countries': 'country1,country2',
    'countries_tags': ['c1', 'c2']
}]
@pytest.mark.parametrize('mongo_db', [(products)], indirect=['mongo_db'])
def test_migrate_with_product_country_selling(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()
    call1 = call(Country, tag='c1', name='country1')
    call2 = call(Country, tag='c2', name='country2')
    mysql_client.get_or_create.assert_has_calls([call1, call2])
    mysql_client.commit.assert_called_once()


products = [{
    'product_name': 'test1',
    'code': 'code_test',
    'lang': 'fr',
    'brands': 'brand1,brand2',
    'brands_tags': ['b1', 'b2']
}]
@pytest.mark.parametrize('mongo_db', [(products)], indirect=['mongo_db'])
def test_migrate_with_product_brand(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()
    call1 = call(Brand, tag='b1', name='brand1')
    call2 = call(Brand, tag='b2', name='brand2')
    mysql_client.get_or_create.assert_has_calls([call1, call2])
    mysql_client.commit.assert_called_once()


products = [{
    'product_name': 'test1',
    'code': 'code_test',
    'lang': 'fr',
    'additives_tags': ['b1', 'b2']
}]
@pytest.mark.parametrize('mongo_db', [(products)], indirect=['mongo_db'])
def test_migrate_with_product_additives(mongo_db, mysql_client):
    migration = Migration(test_config, MagicMock(), mongo_db, mysql_client)
    migration.migrate()
    mongo_db['test'].find.assert_called_once()
    call1 = call(Additive, tag='b1')
    call2 = call(Additive, tag='b2')
    mysql_client.get_or_create.assert_has_calls([call1, call2])
    mysql_client.commit.assert_called_once()
