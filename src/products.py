from abc import abstractmethod, ABC


class AbsProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, price):
        pass

    @classmethod
    @abstractmethod
    def create_and_return(cls):
        """
        Создает новый экземпляр класса и возвращает его
        """
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @staticmethod
    @abstractmethod
    def is_product_in_list(prod, products: list) -> int | None:
        """
        Возвращает номер товара, схожего по имени в списке товаров или None
        """
        pass


class Product(AbsProduct):
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
        s = f"<{self.__class__.__name__}({self.title}, {self.description}, {str(self.__price)}, {str(self.quantity)})>"
        return s

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        """
        Для класса Product необходимо добавить возможность складывать объекты между собой таким образом,
        чтобы результат выполнения сложения двух продуктов был сложением сумм, умноженных на количество на складе.
        Например, для товара с ценой 100 рублей и количеством на складе 10 и товара b c ценой 200 рублей
        и количеством на складе 2 результатом выполнения операции a + b должно стать значение,
        полученное из 100 × 10 + 200 × 2 = 1400.

        Доработать функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых
        классов продуктов. То есть если складывать товар класса «Смартфон» и товар класса «Продукт»,
        то должна быть ошибка типа.
        """
        if isinstance(other, Product) and type(other) == type(self):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError(f"You can't add {type(other)} to {type(self)}")

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (str, Product)):
            raise TypeError("Операнд справа должен иметь тип string или Product")

        return other if isinstance(other, str) else other.title

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.title == sc

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


class Smartphone(Product):
    """
    Помимо имеющихся свойств, необходимо добавить следующие:
    производительность,
    модель,
    объем встроенной памяти,
    цвет.
    """

    def __init__(self, title: str, description: str, price: float, quantity: int,
                 performance: str, model: str, memory: str, color: str):
        super().__init__(title, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Трава газонная
    Помимо имеющихся свойств, необходимо добавить следующие:
    страна-производитель,
    срок прорастания,
    цвет.
    """

    def __init__(self, title: str, description: str, price: float, quantity: int,
                 manufacturer: str, germination_period: str, color: str):
        super().__init__(title, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        self.color = color


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
        if isinstance(product, (Product, Smartphone, LawnGrass)):
            index_if_product_exist = Product.is_product_in_list(product, self.__products)
            if index_if_product_exist is not None:
                merged_successfully = self.merge_products(product, self.__products[index_if_product_exist])
                return merged_successfully
            else:
                self.__products.append(product)
                return True
        else:
            return False

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

    def __str__(self):
        """
        Название категории, количество продуктов: 200 шт.
        Здесь количество продуктов считается из общего числа всех продуктов на складе.
        Для вывода количества на складе лучше использовать магический метод len
        !__len__ реализован для класса Products.
        """
        total_quantity = 0
        for prod in self.__products:
            total_quantity += len(prod)
        return f"{self.title}, количество продуктов: {total_quantity}."

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.title}, {self.description}, {str(self.__products)})>"


class CategoryIterator:
    """
    *** Дополнительное задание**
    Создать новый класс, который принимает на вход категорию
    и дает возможность использовать цикл for для прохода по всем товарам данной категории.

    Заодно поддерживает обращение через [] (CategoryIterator[1] дает 2 продукт (0, 1, 2..)
    И reversed (обратную итерацию), для этого тут __getitem__ и __len__

    Логичнее этот функционал воткнуть в класс Category, но раз нужен новый класс, то пусть будет новый

    """

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current = 0
        return self

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"index must be integer (int). index: {index}")
        if 0 <= index < len(self.category.products):
            return self.category.products[index]
        else:
            raise IndexError(f"Index out of a range (0 <= {index} < {len(self.category.products)}")

    def __len__(self):
        return len(self.category.products)

    def __next__(self):
        if self.current < len(self.category.products):
            number = self.current
            self.current += 1
            return self.category.products[number]
        else:
            raise StopIteration
