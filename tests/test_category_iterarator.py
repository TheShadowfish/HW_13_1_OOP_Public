import pytest
from src.products import CategoryIterator
from src.products import Category
from src.products import Order
from src.products import Product

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