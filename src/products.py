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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    """
    В случае если цена равна или ниже нуля, выведите сообщение в консоль, что цена введена некорректная, 
    при этом новую цену устанавливать не нужно.
    Дополнительное задание (к заданию 4) В случае если цена товара понижается, 
    добавьте логику подтверждения пользователем вручную через ввод y (значит yes) или n (значит no) 
    для согласия понизить цену или для отмены действия соответственно.
    """

    @price.setter
    def price(self, price):

        if price <= 0:
            print(f"Цена введена некорректная.")
            raise ValueError("Цена товара не может быть отрицательной или нулевой")
        elif price < self.__price:
            while True:
                print(f"Товар: {self}, новая цена: {price} (ниже)")
                user_input = input("Вы действительно хотите установить более низкую цену? 'y'- да, 'n'-нет")

                if user_input == 'y':
                    self.__price = price
                    break
                elif user_input == 'n':
                    break

        else:
            self.__price = price

    @classmethod
    def create_and_return(cls, title: str, description: str, price: float, quantity: int):
        new_product = cls(title, description, price, quantity)
        return new_product

    def __str__(self):
        """
        Выводит строку типа: 'Продукт, 80 руб. Остаток: 15 шт.'
        """
        return f"{self.title}, {str(self.__price)}. Остаток: {str(self.quantity)} шт."

    def __repr__(self):
        """
        Выводит строку типа: 'Продукт, 80 руб. Остаток: 15 шт.'
        """
        return f"<{self.title}, {self.description}, {str(self.__price)},{str(self.quantity)}>"

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (str, Product)):
            raise TypeError("Операнд справа должен иметь тип string или Product")

        return other if isinstance(other, str) else other.title

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.title == sc

    """
    Дополнительное задание (к заданию 3) Для данного метода (добавление продукта в список продуктов Category)
    реализуйте проверку наличия такого же товара, схожего по имени. В случае если товар уже существует, необходимо
    сложить количество в наличии старого товара и нового. При конфликте цен выбрать ту, которая является
    более высокой.
    """

    @staticmethod
    def is_product_in_list(prod, products: list) -> int | None:
        """
        Возвращает номер товара, схожего по имени в списке товаров или None
        :param prod: продукт
        :param products: список продуктов
        :return: совпадающий элемент (int) или False
        """
        for i, elem in enumerate(products, start=0):
            if prod == elem:
                return i
        return None


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
            index_if_product_exist = Product.is_product_in_list(product, self.__products)
            if index_if_product_exist is not None:
                merged_successfully = self.merge_products(product, self.__products[index_if_product_exist])
                return merged_successfully
            else:
                self.__products.append(product)
                return True
        else:
            return False

    """
    Дополнительное задание (к заданию 3) Для данного метода (добавление продукта в список продуктов Category)
    реализуйте проверку наличия такого же товара, схожего по имени. В случае если товар уже существует, необходимо
    сложить количество в наличии старого товара и нового. При конфликте цен выбрать ту, которая является
    более высокой.
    """

    @staticmethod
    def merge_products(product, prod_in_list):
        prod_in_list.quantity += product.quantity
        prod_in_list.price = max([prod_in_list.price, product.price])
        return True

    @staticmethod
    def unique_products(products: list[Product]) -> int:
        # Уникальность продукта в категории проверяем по названию
        names_set = []
        for prod in products:
            if str(prod.title) not in names_set:
                names_set.append(prod.title)

        return len(names_set)
