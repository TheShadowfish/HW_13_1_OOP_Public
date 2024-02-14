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
def product_samsung():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


@pytest.fixture
def product_iphone():
    return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)


@pytest.fixture
def product_blackview():
    return Product('Смартфон BV8900, зеленый', '256GB, Green, 10000 mAh, teplovision', 21000.0, 7)


def test_product__init(product_xiaomi):
    """ Корректность инициализации объектов класса Product"""
    assert product_xiaomi.title == 'Xiaomi Redmi Note 11'
    assert product_xiaomi.description == '1024GB, Синий'
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_create_and_return_product():
    assert isinstance(
        Product.create_and_return('Iphone 15', '512GB, Gray space', 210000.0, 8), Product)


def test_product__str(product_blackview):
    assert product_blackview.__str__() == "Смартфон BV8900, зеленый, 21000.0. Остаток: 7 шт."


def test_category__init__(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])

    assert category_phone.title == 'Смартфоны'
    assert category_phone.description == 'описание категории'
    assert isinstance(category_phone.products, list)
    assert len(category_phone.products) == 3


# @pytest.mark.parametrize("product_string", [
#     "Xiaomi Redmi Note 11, 31000.0. Остаток: 14 шт.",
#     "Samsung Galaxy C23 Ultra, 180000.0. Остаток: 5 шт.",
#     "Iphone 15, 210000.0. Остаток: 8 шт."])
def test_category_product_list(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    assert category_phone.product_list
    # assert category_phone.description == 'описание категории'
    for product_str in category_phone.product_list:
        assert isinstance(product_str, str)
    #     # str(product_str) == product_string[i]
    assert len(category_phone.product_list) == 3


def test_add_product(product_xiaomi, product_iphone, product_samsung, product_blackview):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert len(category_phone.product_list) == 3
    #
    assert category_phone.add_product(product_blackview)
    assert not category_phone.add_product("Not product, string")
    assert len(category_phone.product_list) == 4


def test_category_category_count(product_xiaomi, product_iphone, product_samsung):
    """
    Подсчет количества категорий.
    """
    old_cat_count = Category.category_count
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert category_phone
    assert Category.category_count == 1 + old_cat_count


def test_product_count_change__init__(product_xiaomi, product_iphone, product_samsung, product_xiaomi_same_name):
    """
    1. Подсчет количества уникальных продуктов, если продуктов в категории НЕТ
    2. Подсчет количества уникальных продуктов, если названия разные
    3. Подсчет количества уникальных продуктов, если несколько названий в категории совпадают
    """
    # при каждом создании категории этот счетчик растет, поэтому при запуске ВСЕХ тестов приходится проверять
    # НА СКОЛЬКО он увеличился, а не чему он равен
    # иначе тесты будут PASSED только если запускать каждый отдельно
    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории', [])
    assert Category.product_count == 0 + old_prod_count

    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert Category.product_count == 3 + old_prod_count

    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_xiaomi_same_name])
    assert Category.product_count == 2 + old_prod_count
