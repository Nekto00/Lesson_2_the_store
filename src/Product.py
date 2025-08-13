class Product:
    # Атрибуты класса (аннотации типов, необязательные в Python, но полезные для документации)
    name: str  # Название товара
    description: str  # Описание товара
    price: float  # Цена товара (в числовом формате, например, 99.99)
    quantity: int  # Количество товара в наличии

    def __init__(self, name, description, price, quantity):
        """
        Конструктор класса Product. Вызывается при создании нового товара.

        :param name: Название товара (строка)
        :param description: Описание товара (строка)
        :param price: Цена товара (число с плавающей запятой)
        :param quantity: Количество товара (целое число)
        """
        self.name = name  # Устанавливаем название
        self.description = description  # Устанавливаем описание
        self.price = price  # Устанавливаем цену
        self.quantity = quantity  # Устанавливаем количество
