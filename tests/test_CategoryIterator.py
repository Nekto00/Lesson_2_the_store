import pytest

from src.Category import Category
from src.CategoryIterator import CategoryIterator
from src.Product import Product


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

    def test_product_addition(self, sample_products):
        """Тест сложения двух одинаковых продуктов"""
        result = sample_products[0] + sample_products[1]
        assert result.name == "Телефон"
        assert result.quantity == 8  # 5 + 3
        assert result.price == (10000*5 + 8000*3)/8  # Средневзвешенная цена

    def test_addition_with_non_product(self, sample_products):
        """Тест попытки сложения с не-продуктом"""
        with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
            _ = sample_products[0] + 100

    def test_addition_different_products(self, sample_products):
        """Тест попытки сложения разных продуктов"""
        with pytest.raises(ValueError, match="Можно складывать только продукты с одинаковым названием"):
            _ = sample_products[0] + sample_products[2]
