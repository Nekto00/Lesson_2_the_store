import pytest

from src.Category import Category
from src.Product import Product


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.category_total = 0
        Category.product_total = 0

    def test_category_initialization(self):
        """Тест инициализации категории с товарами"""
        # Подготовка
        test_products = [
            Product("Телефон", "Смартфон", 50000, 10),
            Product("Ноутбук", "Игровой", 100000, 5)
        ]

        # Действие
        category = Category("Электроника", "Техника", test_products)

        # Проверка
        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert len(category.products) == 2  # Теперь используем свойство products
        assert category.category_count == 1
        assert category.product_count == 2

    def test_empty_category_initialization(self):
        """Тест инициализации пустой категории"""
        # Действие
        category = Category("Книги", "Литература", [])

        # Проверка
        assert category.name == "Книги"
        assert category.description == "Литература"
        assert len(category.products) == 0
        assert category.category_count == 1
        assert category.product_count == 0

    def test_add_product_to_category(self):
        """Тест добавления товара в категорию"""
        # Подготовка
        category = Category("Одежда", "Мужская", [])
        product = Product("Футболка", "Хлопок", 2000, 20)

        # Действие
        category.add_product(product)

        # Проверка
        assert len(category.products) == 1
        assert category.products[0].name == "Футболка"
        assert category.product_count == 1

    def test_products_info_property(self):
        """Тест свойства products_info"""
        # Подготовка
        products = [
            Product("Чайник", "Электрический", 3000, 15),
            Product("Блендер", "Мощный", 5000, 8)
        ]
        category = Category("Бытовая техника", "Для кухни", products)

        # Действие
        info = category.products_info

        # Проверка
        expected_info = (
            "Чайник, 3000 руб. Остаток: 15 шт.\n"
            "Блендер, 5000 руб. Остаток: 8 шт."
        )
        assert info == expected_info

    def test_empty_products_info(self):
        """Тест свойства products_info для пустой категории"""
        # Подготовка
        category = Category("Мебель", "Для дома", [])

        # Действие
        info = category.products_info

        # Проверка
        assert info == ""

    def test_private_products_attribute(self):
        """Тест приватности атрибута __products"""
        # Подготовка
        category = Category("Игрушки", "Детские", [])

        # Проверка
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_multiple_categories_counter(self):
        """Тест счетчика количества категорий"""
        # Действие
        cat1 = Category("Категория 1", "Описание", [])
        cat2 = Category("Категория 2", "Описание", [])
        cat3 = Category("Категория 3", "Описание", [])

        # Проверка
        assert cat1.category_count == 3
        assert cat2.category_count == 3
        assert cat3.category_count == 3

    def test_products_counter_with_multiple_categories(self):
        """Тест счетчика товаров при нескольких категориях"""
        # Подготовка
        products1 = [
            Product("Товар 1", "Описание", 100, 5),
            Product("Товар 2", "Описание", 200, 3)
        ]
        products2 = [
            Product("Товар 3", "Описание", 300, 2)
        ]

        # Действие
        cat1 = Category("Категория A", "Описание", products1)
        cat2 = Category("Категория B", "Описание", products2)

        # Проверка
        assert cat1.product_count == 3
        assert cat2.product_count == 3

    def test_add_non_product_object(self):
        """Тест добавления не-продукта в категорию"""
        # Подготовка
        category = Category("Спорт", "Инвентарь", [])
        invalid_product = "Футбольный мяч"  # Не объект Product

        # Действие и проверка
        with pytest.raises(AttributeError) as exc_info:
            category.add_product(invalid_product)

        # Дополнительная проверка сообщения об ошибке
        assert "Можно добавлять только объекты класса Product" in str(exc_info.value)
        assert len(category.products) == 0
        assert category.product_count == 0
