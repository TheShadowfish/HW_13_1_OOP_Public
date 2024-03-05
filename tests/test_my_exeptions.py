import pytest
from src.my_exceptions import ProductGroup, AddZeroQuantityProduct, AddNegativeQuantityProduct, AddIncorrectProduct

from src.products import Product
# from src.products import Category
# from src.products import CategoryIterator
# from src.products import Smartphone
# from src.products import LawnGrass
from src.products import Order


def test_add_order_zero_quantity(product_xiaomi, product_iphone, product_samsung):
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])

    product_zero = Product(product_iphone.title, product_iphone.description, product_iphone.price, 0)
    product_negative = Product(product_iphone.title, product_iphone.description, product_iphone.price, -1)

    with pytest.raises(AddIncorrectProduct, match='Можно добавить только экземпляр класса "Товар"'):
        order_phone.add_product("Not product, string")

    with pytest.raises(AddZeroQuantityProduct, match='с нулевым количеством'):
        assert order_phone.add_product(product_zero)

    with pytest.raises(AddNegativeQuantityProduct, match='с ОТРИЦАТЕЛЬНЫМ количеством'):
        assert order_phone.add_product(product_negative)


def test_add_print_outs_right(product_xiaomi, product_iphone, product_samsung, capsys):
    """
    - При этом важно в случае успешного добавления товара вывести сообщение о том, что товар добавлен.
    - Также при любом исходе вывести сообщение, что обработка добавления товара завершена.
    """
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])

    order_phone.add_product(product_samsung)

    captured = capsys.readouterr()

    assert str(captured).find('Товар корректно добавлен') != -1
    assert str(captured).find('Отработка добавления товара завершена') != -1

    assert str(captured).find('А вот этой подстроки в консольном выводе не было и не будет!') == -1


def test_add_print_outs_wrong(product_xiaomi, product_iphone, product_samsung, capsys):
    """
    - При этом важно в случае успешного добавления товара вывести сообщение о том, что товар добавлен.
    - Также при любом исходе вывести сообщение, что обработка добавления товара завершена.
    """
    order_phone = Order([product_xiaomi, product_iphone, product_samsung])

    with pytest.raises(AddIncorrectProduct, match='Можно добавить только экземпляр класса "Товар"'):
        order_phone.add_product("Not product, string")

    captured = capsys.readouterr()

    # такой строки в выводе не будет
    assert str(captured).find('Товар корректно добавлен') == -1

    # А такая будет
    assert str(captured).find('Попытка добавления некорректного экземпляра товара') != -1

    assert str(captured).find('Отработка добавления товара завершена') != -1

    assert str(captured).find('А вот этой подстроки в консольном выводе не было и не будет!') == -1


def test_my_exeptions_raise():
    with pytest.raises(AddZeroQuantityProduct, match='Добавление продукта с нулевым количеством экземпляров.'):
        raise AddZeroQuantityProduct

    with pytest.raises(AddNegativeQuantityProduct,
                       match='Добавление продукта с отрицательным количеством экземпляров.'):
        raise AddNegativeQuantityProduct

    with pytest.raises(AddIncorrectProduct, match='Попытка добавления некорректного экземпляра товара'):
        raise AddIncorrectProduct

    with pytest.raises(ProductGroup, match='Неизвестная ошибка ProductGroup.'):
        raise ProductGroup
