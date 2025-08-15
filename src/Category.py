class Category:
    """
    Класс для представления категории товаров в магазине.
    Содержит общие счетчики для всех категорий и товаров.
    """

    # Атрибуты класса (общие для всех экземпляров)
    name: str  # Название категории (аннотация типа)
    description: str  # Описание категории (аннотация типа)
    products: list  # Список товаров в категории (аннотация типа)
    category_total = 0  # Счетчик общего количества категорий
    product_total = 0  # Счетчик общего количества товаров

    def __init__(self, name: str, description: str, products: list):
        """
        Конструктор класса Category. Инициализирует новую категорию.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики класса при создании новой категории
        Category.category_total += 1  # +1 к общему числу категорий
        Category.product_total += len(products)  # +N к общему числу товаров

    @property
    def category_count(self) -> int:
        """
        Возвращает общее количество созданных категорий.
        Это свойство только для чтения.
        """
        return Category.category_total

    @property
    def product_count(self) -> int:
        """
        Возвращает общее количество всех товаров во всех категориях.
        Это свойство только для чтения.
        """
        return Category.product_total
