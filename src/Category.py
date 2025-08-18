from src.Product import Product


class Category:
    """
    Класс для представления категории товаров в магазине.
    Содержит общие счетчики для всех категорий и товаров.
    """
    name: str
    description: str
    category_total = 0
    product_total = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        Category.category_total += 1
        Category.product_total += len(products)

    @property
    def products(self):
        """Геттер для доступа к списку товаров"""
        return self.__products

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        if not isinstance(product, Product):
            raise AttributeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_total += 1

    @property
    def products_info(self) -> str:
        """Форматированная информация о товарах"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    @property
    def category_count(self) -> int:
        return Category.category_total

    @property
    def product_count(self) -> int:
        return Category.product_total
