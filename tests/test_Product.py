from unittest.mock import patch

import pytest

from src.Product import Product, LawnGrass, Smartphone


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

    def test_private_price_attribute(self):
        """Проверка, что атрибут цены действительно приватный"""
        product = Product("Телефон", "Смартфон", 500.0, 10)

        with pytest.raises(AttributeError):
            # Попытка доступа к приватному атрибуту
            _ = product.__price

    def test_price_setter_negative_value(self, capsys):
        """Проверка, что нельзя установить отрицательную цену"""
        product = Product("Телефон", "Смартфон", 500.0, 10)
        product.price = -100.0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 500.0  # Цена не изменилась

    def test_price_setter_zero_value(self, capsys):
        """Проверка, что нельзя установить нулевую цену"""
        product = Product("Телефон", "Смартфон", 500.0, 10)
        product.price = 0.0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 500.0  # Цена не изменилась

    @patch('builtins.input', return_value='y')
    def test_price_decrease_with_confirmation(self, mock_input, capsys):
        """Проверка понижения цены с подтверждением (пользователь согласен)"""
        product = Product("Телефон", "Смартфон", 500.0, 10)
        product.price = 400.0

        captured = capsys.readouterr()
        assert "Цена успешно изменена на 400.0" in captured.out
        assert product.price == 400.0

    @patch('builtins.input', return_value='n')
    def test_price_decrease_with_rejection(self, mock_input, capsys):
        """Проверка понижения цены с отказом (пользователь не согласен)"""
        product = Product("Телефон", "Смартфон", 500.0, 10)
        product.price = 400.0

        captured = capsys.readouterr()
        assert "Изменение цены отменено" in captured.out
        assert product.price == 500.0  # Цена не изменилась

    def test_price_increase_without_confirmation(self, capsys):
        """Проверка повышения цены без подтверждения"""
        product = Product("Телефон", "Смартфон", 500.0, 10)
        product.price = 600.0

        captured = capsys.readouterr()
        assert "Цена успешно изменена на 600.0" in captured.out
        assert product.price == 600.0

    def test_new_product_method(self):
        """Проверка создания товара через класс-метод"""
        product_data = {
            'name': 'Планшет',
            'description': '10 дюймов',
            'price': 300.0,
            'quantity': 8
        }
        product = Product.new_product(product_data)

        assert product.name == "Планшет"
        assert product.description == "10 дюймов"
        assert product.price == 300.0
        assert product.quantity == 8

    def test_new_product_with_duplicate(self):
        """Проверка обработки дубликатов в new_product"""
        existing_products = [
            Product("Телефон", "Смартфон", 500.0, 10),
            Product("Ноутбук", "Игровой", 1500.0, 5)
        ]

        duplicate_data = {
            'name': 'Телефон',
            'description': 'Новая модель',
            'price': 550.0,
            'quantity': 3
        }

        updated_product = Product.new_product(duplicate_data, existing_products)

        assert updated_product.quantity == 13  # Количества сложились
        assert updated_product.price == 550.0  # Выбрана более высокая цена
        assert updated_product.description == "Новая модель"  # Описание обновилось


class TestLawnGrassFunctionality:
    """Тесты для класса LawnGrass и его методов"""

    def test_lawn_grass_addition_same_name(self):
        """Тест сложения газонной травы с одинаковым названием"""
        grass1 = LawnGrass("Трава", "Газонная", 1500.0, 10, "Россия", 14, "Зеленый")
        grass2 = LawnGrass("Трава", "Газонная", 1600.0, 5, "Россия", 14, "Зеленый")

        result = grass1 + grass2
        assert isinstance(result, LawnGrass)
        assert result.name == "Трава"
        assert result.quantity == 15
        assert result.price == (1500.0 * 10 + 1600.0 * 5) / 15
        assert result.country == "Россия"
        assert result.germination_period == 14

    def test_lawn_grass_addition_different_classes_error(self):
        """Тест ошибки при сложении LawnGrass с другим классом"""
        grass = LawnGrass("Трава", "Газонная", 1500.0, 10, "Россия", 14, "Зеленый")
        smartphone = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")

        with pytest.raises(TypeError, match="Можно складывать только объекты класса LawnGrass"):
            grass + smartphone


class TestSmartphoneFunctionality:
    """Тесты для класса Smartphone и его методов"""

    def test_smartphone_addition_same_name(self):
        """Тест сложения смартфонов с одинаковым названием"""
        phone1 = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")
        phone2 = Smartphone("iPhone", "Смартфон", 95000.0, 2, 95.5, "15 Pro", 256, "Синий")

        result = phone1 + phone2
        assert isinstance(result, Smartphone)
        assert result.name == "iPhone"
        assert result.quantity == 5
        assert result.price == (90000.0 * 3 + 95000.0 * 2) / 5
        assert result.efficiency == 95.5
        assert result.model == "15 Pro"

    def test_smartphone_addition_different_names(self):
        """Тест сложения смартфонов с разными названиями"""
        phone1 = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")
        phone2 = Smartphone("Samsung", "Смартфон", 80000.0, 4, 92.3, "S23", 128, "Черный")

        result = phone1 + phone2
        expected_total = 90000.0 * 3 + 80000.0 * 4
        assert result == expected_total

    def test_smartphone_addition_different_classes_error(self):
        """Тест ошибки при сложении Smartphone с другим классом"""
        smartphone = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")
        product = Product("Ноутбук", "Игровой ноутбук", 50000.0, 5)

        with pytest.raises(TypeError, match="Можно складывать только объекты класса Smartphone"):
            smartphone + product