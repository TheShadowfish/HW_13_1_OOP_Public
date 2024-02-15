import json
import pytest
from src.json_parser import json_parse


@pytest.fixture
def json_to_categories():
    json_dict = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]

    return json_dict


def test_json_parse(json_to_categories):
    """ Корректность получения экземпляров Category Product из файла JSON"""
    cat_list = json_parse(json_to_categories)[0]

    assert cat_list.title == 'Телевизоры'
    assert cat_list.description == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
    assert cat_list.products[0].title == "55\" QLED 4K"
    assert cat_list.products[0].description == "Фоновая подсветка"
    assert cat_list.products[0].price == 123000.0
    assert cat_list.products[0].quantity == 7
