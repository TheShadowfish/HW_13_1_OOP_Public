import pytest

from src.products import Product
from src.products import Category
from src.products import CategoryIterator
from src.products import Smartphone
from src.products import LawnGrass
from src.products import Order

from src.my_exceptions import AddZeroQuantityProduct, AddNegativeQuantityProduct, AddIncorrectProduct


def test_category__init__(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])

    assert category_phone.title == 'Смартфоны'
    assert category_phone.description == 'описание категории'
    assert isinstance(category_phone.products, list)
    assert len(category_phone.products) == 3


def test_category_product_list(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    assert category_phone.product_list
    for product_str in category_phone.product_list:
        assert isinstance(product_str, str)
    assert len(category_phone.product_list) == 3


def test_add_product(product_xiaomi, product_iphone, product_samsung, product_blackview, smartphone, lawngrass):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert len(category_phone.product_list) == 3

    assert category_phone.add_product(product_blackview) is None

    assert len(category_phone.product_list) == 4

    assert category_phone.add_product(lawngrass) is None
    assert len(category_phone.product_list) == 5

    # assert not category_phone.add_product("Not product, string")

    assert category_phone.add_product(smartphone) is None
    assert len(category_phone.product_list) == 6


def test_add_product_zero_quantity(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    product_zero = Product(product_iphone.title, product_iphone.description, product_iphone.price, 0)
    product_negative = Product(product_iphone.title, product_iphone.description, product_iphone.price, -1)

    # Просили ПРЕРЫВАТЬ работу программы, значит будем прерывать
    with pytest.raises(SystemExit):
        assert category_phone.add_product(product_zero)

    with pytest.raises(SystemExit):
        assert category_phone.add_product(product_negative)

    with pytest.raises(SystemExit):
        assert category_phone.add_product("Not product, string")

    # with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
    #     assert category_phone.add_product(product_zero)
    #
    # with pytest.raises(ValueError, match='с ОТРИЦАТЕЛЬНЫМ количеством'):
    #     assert category_phone.add_product(product_negative)


def test_add_product_is_yet(product_xiaomi, product_iphone, product_samsung, product_xiaomi_same_name):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    quantity = product_xiaomi.quantity + product_xiaomi_same_name.quantity
    price = max([product_xiaomi.price, product_xiaomi_same_name.price])

    assert len(category_phone.product_list) == 3
    #
    assert category_phone.add_product(product_xiaomi_same_name) is None
    # assert not category_phone.add_product("Not product, string")
    assert len(category_phone.product_list) == 3
    assert category_phone.products[0].quantity == quantity
    assert category_phone.products[0].price == price
    assert price == 35000.0


def test_product_avg(product_xiaomi, product_iphone, product_samsung, product_xiaomi_same_name):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    category_phone_no_products = Category('Смартфоны', 'описание категории',
                                          [])

    # ничего, что средний ценник на количество нормально не делится из-за float?
    # 140333.33333333334 != 140333

    avg = (product_xiaomi.price + product_iphone.price + product_samsung.price) / 3

    assert category_phone.products_avg() == avg
    assert category_phone_no_products.products_avg() == 0


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
    assert category_phone

    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert Category.product_count == 3 + old_prod_count
    assert category_phone

    old_prod_count = Category.product_count
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_xiaomi_same_name])
    assert Category.product_count == 2 + old_prod_count
    assert category_phone


def test_category__str__(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert category_phone.__str__() == "Смартфоны, количество продуктов: 27."
    # assert category_phone.__repr__() == ("<Category(Смартфоны, описание категории, [<Product(Xiaomi Redmi Note 11, "
    #                                      "1024GB, Синий, 31000.0, 14)>, <Product(Iphone 15, 512GB, Gray space, "
    #                                      "210000.0, 8)>, <Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, "
    #                                      "200MP камера, 180000.0, 5)>])>")

    # assert print(category_phone) == 'Смартфоны, количество продуктов: 27.'


def test_order__init__(product_xiaomi, lawngrass):
    order_1 = Order([lawngrass, lawngrass])
    order_2 = Order([lawngrass])
    order_3 = Order(lawngrass)
    order_4 = Order([product_xiaomi, lawngrass])

    # assert isinstance(order_1.products, list)
    # assert len(order_1.products) == 1

    assert order_1.quantity == 2
    assert order_1.price == 14000
    assert len(order_1.products) == 2

    assert order_2.quantity == 1
    assert order_2.price == 7000

    assert order_3.quantity == 1
    assert order_3.price == 7000
    assert isinstance(order_3.products, list)

    assert order_4.quantity == 15
    assert order_4.price == 7000 + 14 * 31000.0
    assert len(order_4.products) == 2


def test_order_product_list(product_xiaomi, lawngrass):
    order = Order([product_xiaomi, lawngrass])

    assert order.product_list
    # assert category_phone.description == 'описание категории'
    for product_str in order.product_list:
        assert isinstance(product_str, str)
    #     # str(product_str) == product_string[i]
    assert len(order.product_list) == 2


def test_add_order(product_xiaomi, product_iphone, product_samsung, product_blackview, smartphone, lawngrass):
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])
    assert len(order_phone.product_list) == 3

    assert order_phone.add_product(product_blackview) is None

    assert len(order_phone.product_list) == 4

    assert order_phone.add_product(lawngrass) is None
    assert len(order_phone.product_list) == 5

    # assert not order_phone.add_product("Not product, string")

    assert order_phone.add_product(smartphone) is None
    assert len(order_phone.product_list) == 6


def test_add_order_zero_quantity(product_xiaomi, product_iphone, product_samsung):
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])

    product_zero = Product(product_iphone.title, product_iphone.description, product_iphone.price, 0)
    product_negative = Product(product_iphone.title, product_iphone.description, product_iphone.price, -1)

    # with pytest.raises(AddZeroQuantityProduct) as exec_info:
    #     order_phone.add_product(product_zero)
    #     print(exec_info)
    #     #assert AddZeroQuantityProduct in str(exec_info.value) == 'нулевым'
    #     #self.message = args[0] if args else 'Добавление продукта с нулевым количеством экземпляров.'
    # with pytest.raises(AddZeroQuantityProduct, match='с ОТРИЦАТЕЛЬНЫМ количеством'):
    #     assert order_phone.add_product(product_negative)
    # with pytest.raises(ValueError):
    #     order_phone.add_product(product_zero)

    with pytest.raises(ValueError, match='Можно добавить только экземпляр класса "Товар"'):
        order_phone.add_product("Not product, string")

    with pytest.raises(ValueError, match='с нулевым количеством не может быть добавлен'):
        assert order_phone.add_product(product_zero)

    with pytest.raises(ValueError, match='с ОТРИЦАТЕЛЬНЫМ количеством'):
        assert order_phone.add_product(product_negative)


def test_add_order_product_is_yet(product_xiaomi, product_iphone, product_samsung, product_xiaomi_same_name, lawngrass):
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])

    quantity = product_xiaomi.quantity + product_xiaomi_same_name.quantity
    price = max([product_xiaomi.price, product_xiaomi_same_name.price])

    assert len(order_phone.product_list) == 3
    #
    assert order_phone.add_product(product_xiaomi_same_name) is None
    # assert not order_phone.add_product("Not product, string")
    assert len(order_phone.product_list) == 3
    assert order_phone.products[0].quantity == quantity
    assert order_phone.products[0].price == price
    assert price == 35000.0
    #
    order_lawn = Order(lawngrass)
    assert order_lawn.add_product(lawngrass) is None
    assert len(order_lawn.product_list) == 1
    assert order_lawn.quantity == 2
    assert order_lawn.price == 14000.0


def test_order__str__(lawngrass, product_iphone, product_samsung):
    order = Order([lawngrass, product_iphone, product_samsung])
    assert order.__str__() == f"Количество продуктов: 14, общая стоимость {7000.0 + 210000.0 * 8 + 180000.0 * 5}."
