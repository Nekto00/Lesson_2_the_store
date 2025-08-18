class CategoryIterator:
    """Класс-итератор для перебора товаров категории"""

    def __init__(self, category):
        """
        Инициализация итератора

        :param category: Объект категории для итерации
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект итератора"""
        return self

    def __next__(self):
        """
        Возвращает следующий товар в категории

        :return: Следующий товар (объект Product)
        :raises StopIteration: Когда товары закончились
        """
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
