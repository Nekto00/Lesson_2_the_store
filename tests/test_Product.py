import pytest

from src.Product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Проверка инициализации продукта"""
        product = Product("Телефон", "Смартфон", 500.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 500.0
        assert product.quantity == 10

    @pytest.mark.parametrize("name,description,price,quantity", [
        ("Телефон", "Смартфон", 500.0, 10),
        ("Ноутбук", "Игровой", 1500.0, 5),
        ("Наушники", "Беспроводные", 200.0, 20)
    ])
    def test_product_variations(self, name, description, price, quantity):
        """Параметризованный тест для разных продуктов"""
        product = Product(name, description, price, quantity)

        assert product.name == name
        assert product.description == description
        assert product.price == price
        assert product.quantity == quantity
