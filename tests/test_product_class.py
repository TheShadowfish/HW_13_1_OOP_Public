import pytest
import mock  # для тестирования функции с пользовательским вводом    test_product_lower_price_dialog()
import builtins  # для тестирования функции с пользовательским вводом

from src.products import Product

def test_smartphone__init(smartphone):
    """ Корректность инициализации объектов класса Product"""
    assert smartphone.title == 'Xiaomi Redmi Note 11 (Pro)'
    assert smartphone.description == '1024GB, Синий'
    assert smartphone.price == 31000.0
    assert smartphone.quantity == 14
    assert smartphone.performance == 'high'
    assert smartphone.model == 'Xiaomi Redmi Note 11'
    assert smartphone.memory == '1024GB'
    assert smartphone.color == 'Синий'


def test_lawngrass__init(lawngrass):
    """ Корректность инициализации объектов класса Product"""
    assert lawngrass.title == 'Трава газонная голландская'
    assert lawngrass.description == 'Можно любоваться, можно курить'
    assert lawngrass.price == 7000.0
    assert lawngrass.quantity == 1
    assert lawngrass.manufacturer == 'Голландия'
    assert lawngrass.germination_period == '2 недели'
    assert lawngrass.color == 'Темно-зеленый'


def test_product__init(product_xiaomi):
    """ Корректность инициализации объектов класса Product"""
    assert product_xiaomi.title == 'Xiaomi Redmi Note 11'
    assert product_xiaomi.description == '1024GB, Синий'
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_product_lower_price_dialog(product_xiaomi):
    product_xiaomi.price = 33000.0
    assert product_xiaomi.price == 33000.0

    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        product_xiaomi.price = 30000.0
        assert product_xiaomi.price == 33000.0

    with mock.patch.object(builtins, 'input', lambda _: 'not y'):
        product_xiaomi.price = 30000.0
        assert product_xiaomi.price == 33000.0

    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        product_xiaomi.price = 30000.0
        assert product_xiaomi.price == 30000.0


def test_create_and_return_product():
    assert isinstance(
        Product.create_and_return('Iphone 15', '512GB, Gray space', 210000.0, 8), Product)


def test_product__str(product_blackview):
    assert product_blackview.__str__() == "Смартфон BV8900, зеленый, 21000.0. Остаток: 7 шт."
    # assert product_blackview.__repr__() == ('<Product(Смартфон BV8900, зеленый, 256GB, Green,'
    #                                         ' 10000 mAh, teplovision, '
    #                                         '21000.0, 7)>')


def test_product__add(product_xiaomi, product_iphone, smartphone, lawngrass):
    assert product_xiaomi.__add__(product_iphone) == 2114000.0
    assert smartphone.__add__(smartphone) == 868000.0
    assert lawngrass.__add__(lawngrass) == 14000.0
    with pytest.raises(TypeError):
        product_xiaomi.__add__('Xiaomi Redmi Note 9')
    with pytest.raises(TypeError):
        product_xiaomi.__add__(smartphone)
    with pytest.raises(TypeError):
        product_xiaomi.__add__(lawngrass)
    with pytest.raises(TypeError):
        lawngrass.__add__(smartphone)


def test_incorrect_price(product_iphone):
    with pytest.raises(ValueError):
        product_iphone.price = -1


def test_product__eg__(product_xiaomi, product_xiaomi_same_name):
    assert product_xiaomi == product_xiaomi
    assert product_xiaomi == product_xiaomi_same_name
    assert product_xiaomi == 'Xiaomi Redmi Note 11'
    assert not product_xiaomi == 'Xiaomi Redmi Note 9'
    assert not product_xiaomi == 'fgsfds'
    with pytest.raises(TypeError):
        product_xiaomi.__eq__(None)
    with pytest.raises(TypeError):
        product_xiaomi.__eq__(1100342432)


def test_is_product_in_list(product_xiaomi, product_xiaomi_same_name, product_samsung, product_iphone):
    assert Product.is_product_in_list(product_xiaomi, [product_iphone, product_samsung]) is None
    assert Product.is_product_in_list(product_xiaomi, []) is None
    assert Product.is_product_in_list(product_xiaomi, [product_iphone, product_xiaomi_same_name]) == 1
    assert Product.is_product_in_list(product_xiaomi, ['prod1', 'prod2', 'Xiaomi Redmi Note 11', 'prod3']) == 2
    assert Product.is_product_in_list('Xiaomi Redmi Note 11', [product_iphone, product_xiaomi_same_name]) == 1