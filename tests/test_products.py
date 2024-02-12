import pytest

from src.products import Product
from src.products import Category

@pytest.fixture
def product_xiaomi():
    return Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)

@pytest.fixture
def product_xiaomi_same_name():
    return Product('Xiaomi Redmi Note 11', '1024GB, Серебрянный', 31000.0, 10)

@pytest.fixture
def product_iphone():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)

@pytest.fixture
def product_samsung():
    return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)

test_title = 'Смартфоны'
test_description = 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_product__init(product_xiaomi):
    """ Корректность инициализации объектов класса Product"""
    assert product_xiaomi.title == 'Xiaomi Redmi Note 11'
    assert product_xiaomi.description == '1024GB, Синий'
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14

def test_category__init__(product_xiaomi, product_iphone, product_samsung):

    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])

    assert category_phone.title == 'Смартфоны'
    assert category_phone.description == 'описание категории'
    assert isinstance(category_phone.products, list)
    assert len(category_phone.products) == 3

def test_category_category_count(product_xiaomi, product_iphone, product_samsung):
    """
    Подсчет количества категорий.
    """
    old_cat_count = Category.category_count
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])
    assert Category.category_count == 1 + old_cat_count

def test_category_product_count(product_xiaomi, product_iphone, product_samsung):
    """
    Подсчет количества продуктов,
    Подсчет количества категорий.
    """
    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])
    assert Category.product_count == 3 + old_prod_count

def test_unique_products(product_xiaomi, product_iphone, product_xiaomi_same_name):
    """
    Подсчет количества продуктов,
    Подсчет количества категорий.
    """
    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_xiaomi_same_name])
    assert Category.product_count == 2 + old_prod_count

