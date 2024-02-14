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

    @classmethod
    def create_and_return(cls, title: str, description: str, price: float, quantity: int):
        new_product = cls(title, description, price, quantity)
        return new_product

    def __str__(self):
        """
        Выводит строку типа: 'Продукт, 80 руб. Остаток: 15 шт.'
        """
        return f"{self.title}, {str(self.price)}. Остаток: {str(self.quantity)} шт."

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (str, Product)):
            raise TypeError("Операнд справа должен иметь тип datetime или Operation")

        return other if isinstance(other, str) else other.title

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.title == sc


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
        self.__products = products

        Category.category_count += 1

        # Category.product_count += len(set(self.products))
        Category.product_count += Category.unique_products(self.__products)

    @property
    def products(self):
        return self.__products

    @property
    def product_list(self):
        products_strings = []
        for prod in self.__products:
            products_strings.append(str(prod))
        return products_strings

    def add_product(self, product: Product):
        """Добавление продукта в список."""
        if isinstance(product, Product):
            self.__products.append(product)
            return True
        else:
            return False

    @staticmethod
    def unique_products(products: list[Product]) -> int:
        # Уникальность продукта в категории проверяем по названию
        names_set = []
        for prod in products:
            if str(prod.title) not in names_set:
                names_set.append(prod.title)

        return len(names_set)
