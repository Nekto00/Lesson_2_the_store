import pytest

from src.Category import Category
from src.CategoryIterator import CategoryIterator
from src.Product import Product, Smartphone


class TestCategoryIteration:
    @pytest.fixture
    def sample_category(self):
        products = [
            Product("Телефон", "Смартфон", 10000, 5),
            Product("Ноутбук", "Игровой", 50000, 2),
            Product("Планшет", "10 дюймов", 20000, 3)
        ]
        return Category("Электроника", "Техника", products)

    def test_for_loop_iteration(self, sample_category):
        """Тест итерации в цикле for"""
        products = [product.name for product in sample_category]
        assert products == ["Телефон", "Ноутбук", "Планшет"]

    def test_multiple_iterators(self, sample_category):
        """Тест независимости нескольких итераторов"""
        iter1 = iter(sample_category)
        iter2 = iter(sample_category)

        assert next(iter1).name == "Телефон"
        assert next(iter2).name == "Телефон"
        assert next(iter1).name == "Ноутбук"
        assert next(iter2).name == "Ноутбук"

    def test_empty_category(self):
        """Тест итерации по пустой категории"""
        empty_category = Category("Пустая", "Нет товаров", [])
        assert list(empty_category) == []

    def test_iterator_protocol(self, sample_category):
        """Тест протокола итератора"""
        iterator = iter(sample_category)
        assert isinstance(iterator, CategoryIterator)

        products = []
        while True:
            try:
                products.append(next(iterator).name)
            except StopIteration:
                break

        assert products == ["Телефон", "Ноутбук", "Планшет"]


class TestProductAddition:
    @pytest.fixture
    def sample_products(self):
        return [
            Product("Телефон", "Смартфон", 10000, 5),
            Product("Телефон", "Смартфон", 8000, 3),
            Product("Ноутбук", "Игровой", 50000, 2)
        ]

    def test_product_addition_same_class(self):
        """Тест сложения объектов одного класса Product"""
        product1 = Product("Ноутбук", "Игровой ноутбук", 50000.0, 5)
        product2 = Product("Ноутбук", "Игровой ноутбук", 60000.0, 3)

        result = product1 + product2
        expected_total = 50000.0 * 5 + 60000.0 * 3
        assert result == expected_total

    def test_product_addition_different_names(self):
        """Тест сложения объектов Product с разными названиями"""
        product1 = Product("Ноутбук", "Игровой ноутбук", 50000.0, 5)
        product2 = Product("Мышь", "Беспроводная мышь", 2500.0, 10)

        result = product1 + product2
        expected_total = 50000.0 * 5 + 2500.0 * 10
        assert result == expected_total

    def test_product_addition_different_classes_error(self):
        """Тест ошибки при сложении Product с другим классом"""
        product = Product("Ноутбук", "Игровой ноутбук", 50000.0, 5)
        smartphone = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")

        with pytest.raises(TypeError, match="Нельзя складывать товары из разных классов продуктов"):
            product + smartphone

    def test_addition_with_non_product(self, sample_products):
        """Тест попытки сложения с не-продуктом"""
        with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
            _ = sample_products[0] + 100
