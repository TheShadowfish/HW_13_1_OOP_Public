import pytest

from src.products import Product
from src.products import Category
from src.products import CategoryIterator
from src.products import Smartphone
from src.products import LawnGrass


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
    return LawnGrass('Трава газонная голландская', 'Можно любоваться, можно курить', 7000.0, 22,
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
    assert lawngrass.quantity == 22
    assert lawngrass.manufacturer == 'Голландия'
    assert lawngrass.germination_period == '2 недели'
    assert lawngrass.color == 'Темно-зеленый'


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
    # assert product_blackview.__repr__() == ('<Product(Смартфон BV8900, зеленый, 256GB, Green, 10000 mAh, teplovision, '
    #                                         '21000.0, 7)>')


def test_product__add(product_xiaomi, product_iphone, smartphone, lawngrass):
    assert product_xiaomi.__add__(product_iphone) == 2114000.0
    assert smartphone.__add__(smartphone) == 868000.0
    assert lawngrass.__add__(lawngrass) == 308000.0
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


#
# def test_operation__verify_data(one_right_dict_fixture):
#     op1 = Operation(one_right_dict_fixture)
#     with pytest.raises(TypeError):
#         op1.__eq__('no_operation_no_datetime')


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


def test_add_product(product_xiaomi, product_iphone, product_samsung, product_blackview, smartphone, lawngrass):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])
    assert len(category_phone.product_list) == 3

    assert category_phone.add_product(product_blackview)

    assert len(category_phone.product_list) == 4

    assert category_phone.add_product(lawngrass)
    assert len(category_phone.product_list) == 5

    assert not category_phone.add_product("Not product, string")

    assert category_phone.add_product(smartphone)
    assert len(category_phone.product_list) == 6


def test_add_product_is_yet(product_xiaomi, product_iphone, product_samsung, product_xiaomi_same_name):
    category_phone = Category('Смартфоны', 'описание категории',
                              [product_xiaomi, product_iphone, product_samsung])

    quantity = product_xiaomi.quantity + product_xiaomi_same_name.quantity
    price = max([product_xiaomi.price, product_xiaomi_same_name.price])

    assert len(category_phone.product_list) == 3
    #
    assert category_phone.add_product(product_xiaomi_same_name)
    # assert not category_phone.add_product("Not product, string")
    assert len(category_phone.product_list) == 3
    assert category_phone.products[0].quantity == quantity
    assert category_phone.products[0].price == price
    assert price == 35000.0


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


def test_category_iterator__init__(product_xiaomi, product_iphone, product_samsung):
    category_phone = Category('Смартфоны', 'описание категории', [product_xiaomi, product_iphone, product_samsung])
    cat_iterator = CategoryIterator(category_phone)
    assert isinstance(cat_iterator, CategoryIterator)
    assert isinstance(cat_iterator.category.products, list)
    assert cat_iterator.category is category_phone

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
