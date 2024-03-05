import pytest

from src.products import Product
from src.products import Category
from src.products import CategoryIterator
from src.products import Smartphone
from src.products import LawnGrass
from src.products import Order

from src.my_exceptions import AddZeroQuantityProduct, AddNegativeQuantityProduct, AddIncorrectProduct


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