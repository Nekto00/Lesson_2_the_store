class Product:
    """
    Класс для представления товара в магазине.
    """
    name: str
    description: str
    __price: float  # Приватный атрибут цены
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Конструктор класса Product.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара (должна быть положительной)
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = 0.0  # Инициализируем нулем
        self.price = price  # Используем сеттер для установки цены с проверкой
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер для получения цены товара.

        :return: Текущая цена товара
        """
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Сеттер для установки цены товара с проверками:
        1. Цена должна быть положительной
        2. При понижении цены требует подтверждения
        """
        # Проверка на отрицательную или нулевую цену
        if new_price <= 0:
            print("Ошибка: Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if new_price < self.__price:
            answer = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        # Если все проверки пройдены, устанавливаем новую цену
        self.__price = new_price
        print(f"Цена успешно изменена на {new_price}")

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):
        """
        Класс-метод для создания нового товара или обновления существующего.

        :param product_data: Словарь с параметрами товара
        :param products: Список существующих товаров для проверки дубликатов
        :return: Объект класса Product (новый или обновленный)
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = float(product_data.get('price'))
        quantity = int(product_data.get('quantity'))

        # Если передан список товаров, ищем дубликаты
        if products:
            for existing_product in products:
                if existing_product.name.lower() == name.lower():
                    # Объединяем количество
                    existing_product.quantity += quantity
                    # Выбираем максимальную цену
                    existing_product.price = max(existing_product.price, price)
                    # Обновляем описание, если оно было изменено
                    if description:
                        existing_product.description = description
                    return existing_product

        # Если дубликатов не найдено, создаем новый товар
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод для сложения продуктов.
        Можно складывать только товары из одинаковых классов.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        # Проверяем, что объекты одного класса
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары из разных классов продуктов")

        # Для продуктов одного класса возвращаем общую стоимость
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """
    Класс для представления смартфона в магазине.
    Наследуется от класса Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
             efficiency: float, model: str, memory: int, color: str):
        """
        Конструктор класса Smartphone.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        :param efficiency: Производительность
        :param model: Модель смартфона
        :param memory: Объем встроенной памяти (ГБ)
        :param color: Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def str(self) -> str:
        return (f"{self.name} ({self.model}), {self.price} руб. "
                f"Память: {self.memory}ГБ, Цвет: {self.color}, "
                f"Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только объекты класса Smartphone")

        if self.name == other.name:
            # Для одинаковых смартфонов - объединяем
            total_quantity = self.quantity + other.quantity
            average_price = (self.price * self.quantity + other.price * other.quantity) / total_quantity

            return Smartphone(
                name=self.name,
                description=self.description,
                price=average_price,
                quantity=total_quantity,
                efficiency=self.efficiency,
                model=self.model,
                memory=self.memory,
                color=self.color
            )
        else:
            # Для разных смартфонов - возвращаем общую стоимость
            return self.price * self.quantity + other.price * other.quantity


class LawnGrass(Product):
    """
    Класс для представления газонной травы в магазине.
    Наследуется от класса Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        """
        Конструктор класса LawnGrass.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        :param country: Страна-производитель
        :param germination_period: Срок прорастания (в днях)
        :param color: Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return (f"{self.name}, {self.price} руб. "
                f"Страна: {self.country}, Срок прорастания: {self.germination_period} дней, "
                f"Цвет: {self.color}, Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError("Можно складывать только объекты класса LawnGrass")

        if self.name == other.name:
            # Для одинаковой газонной травы - объединяем
            total_quantity = self.quantity + other.quantity
            average_price = (self.price * self.quantity + other.price * other.quantity) / total_quantity

            return LawnGrass(
                name=self.name,
                description=self.description,
                price=average_price,
                quantity=total_quantity,
                country=self.country,
                germination_period=self.germination_period,
                color=self.color
            )
        else:
            # Для разной газонной травы - возвращаем общую стоимость
            return self.price * self.quantity + other.price * other.quantity
