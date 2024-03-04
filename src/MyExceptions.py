class ProductGroup(ValueError):
    """Общий класс исключения для наследников ProductGroup (Category, Order)"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка ProductGroup.'

    def __str__(self):
        return self.message


class AddZeroQuantityProduct(ProductGroup):
    """Класс исключения при добавлении продукта с нулевым количеством экземпляров"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Добавление продукта с нулевым количеством экземпляров.' #
        # self.message = 'Добавление продукта с нулевым количеством экземпляров.'

        def __str__(self):
            return self.message

class AddNegativeQuantityProduct(ProductGroup):
    """Класс исключения при добавлении продукта с нулевым количеством экземпляров"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Добавление продукта с отрицательным количеством экземпляров.'