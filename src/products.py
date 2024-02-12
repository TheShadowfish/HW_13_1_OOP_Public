import copy

class Product:
    """
    Продукты. Поля класса:
    - title: название
    - description: описание
    - price: цена
    - quantity: количество в наличии
    """

    def __init__(self, title: str, description: str, price: float, quantity: int):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """
    Категория продуктов. Поля класса:
    - title: название
    - description: описание
    - products: товары

    Аттрибуты класса:
    - category_count: общее количество категорий
    - product_count: общее количество уникальных продуктов, не учитывая количество в наличии.
    """
    category_count = 0
    product_count = 0

    def __init__(self, title: str, description: str, products: list[Product]):
        self.title = title
        self.description = description
        self.products = products


        Category.category_count += 1

        # Category.product_count += len(set(self.products))
        Category.product_count += Category.unique_products(self.products)


    @classmethod
    def unique_products(cls, products: list[Product])-> int:
        # Уникальность продукта в категории проверяем по названию
        names_set = []
        for prod in products:
            if str(prod.title) not in names_set:
                names_set.append(prod.title)

        return len(names_set)





