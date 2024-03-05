import pytest
import mock  # для тестирования функции с пользовательским вводом    test_product_lower_price_dialog()
import builtins  # для тестирования функции с пользовательским вводом

from src.products import Product
from src.products import Category
from src.products import CategoryIterator
from src.products import Smartphone
from src.products import LawnGrass
from src.products import Order
# from src.products import AddZeroQuantityProduct


@pytest.fixture
def product_xiaomi():
    return Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)


@pytest.fixture
def product_xiaomi_same_name():
    return Product('Xiaomi Redmi Note 11', '1024GB, Серебрянный', 35000.0, 10)


@pytest.fixture
def product_samsung():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


@pytest.fixture
def product_iphone():
    return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)


@pytest.fixture
def product_blackview():
    return Product('Смартфон BV8900, зеленый', '256GB, Green, 10000 mAh, teplovision', 21000.0, 7)


@pytest.fixture
def smartphone():
    return Smartphone('Xiaomi Redmi Note 11 (Pro)', '1024GB, Синий', 31000.0, 14,
                      'high', 'Xiaomi Redmi Note 11', '1024GB', 'Синий')


@pytest.fixture
def lawngrass():
    return LawnGrass('Трава газонная голландская', 'Можно любоваться, можно курить', 7000.0, 1,
                     'Голландия', '2 недели', 'Темно-зеленый')


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

    with pytest.raises(ValueError, match= 'Можно добавить только экземпляр класса "Товар"'):
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


    # with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
    #     assert category_phone.add_product(product_zero)
    #
    # with pytest.raises(ValueError, match='с ОТРИЦАТЕЛЬНЫМ количеством'):
    #     assert category_phone.add_product(product_negative)

def test_order__str__(lawngrass, product_iphone, product_samsung):
    order = Order([lawngrass, product_iphone, product_samsung])
    assert order.__str__() == f"Количество продуктов: 14, общая стоимость {7000.0 + 210000.0 * 8 + 180000.0 * 5}."


def test_category_iterator__init__(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])
    cat_iterator = CategoryIterator(category_phone)
    assert isinstance(cat_iterator, CategoryIterator)
    assert isinstance(cat_iterator.category.products, list)
    assert cat_iterator.category is category_phone

    order_phone = Order([product_xiaomi, product_iphone, product_samsung])
    ord_iterator = CategoryIterator(order_phone)
    assert isinstance(ord_iterator, CategoryIterator)
    assert isinstance(ord_iterator.category.products, list)
    assert ord_iterator.category is order_phone

    # assert CategoryIterator(category_phone)
    # assert category_phone.title == 'Смартфоны'
    # assert category_phone.description == 'описание категории'
    # assert isinstance(category_phone.products, list)
    # assert len(category_phone.products) == 3


def test_category_iterator_iteration_reverse_getitem(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])
    cat_iterator = CategoryIterator(category_phone)

    assert cat_iterator[1] is product_iphone
    with pytest.raises(IndexError):
        cat_iterator[-1]
    with pytest.raises(IndexError):
        cat_iterator[3]
    with pytest.raises(TypeError):
        cat_iterator['Lizard']

    for i, prod in enumerate(cat_iterator, start=0):
        assert isinstance(prod, Product)
        assert prod is category_phone.products[i]

    for i, prod in enumerate(reversed(cat_iterator), start=1):
        assert isinstance(prod, Product)
        assert prod is category_phone.products[3 - i]
