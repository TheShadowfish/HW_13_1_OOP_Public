import pytest
from src.my_exceptions import ProductGroup, AddZeroQuantityProduct, AddNegativeQuantityProduct, AddIncorrectProduct


from src.products import Product
from src.products import Category
from src.products import CategoryIterator
from src.products import Smartphone
from src.products import LawnGrass
from src.products import Order

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



def test_my_exeptions_raise():

    with pytest.raises(AddZeroQuantityProduct, match='Добавление продукта с нулевым количеством экземпляров.'):
        raise AddZeroQuantityProduct

    with pytest.raises(AddNegativeQuantityProduct, match='Добавление продукта с отрицательным количеством экземпляров.'):
        raise AddNegativeQuantityProduct

    with pytest.raises(AddIncorrectProduct, match='Попытка добавления некорректного экземпляра товара'):
        raise AddIncorrectProduct

    with pytest.raises(ProductGroup, match='Неизвестная ошибка ProductGroup.'):
        raise ProductGroup
