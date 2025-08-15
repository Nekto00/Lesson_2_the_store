from src.Category import Category


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.category_total = 0
        Category.product_total = 0

    def test_category_initialization(self):
        """Проверка инициализации категории"""
        cat = Category("Электроника", "Техника", ["Телефон", "Ноутбук"])

        assert cat.name == "Электроника"
        assert cat.description == "Техника"
        assert cat.products == ["Телефон", "Ноутбук"]

    def test_category_counter(self):
        """Проверка счетчика категорий"""
        assert Category.category_total == 0

        cat1 = Category("Категория 1", "Описание", [])
        assert cat1.category_count == 1

        cat2 = Category("Категория 2", "Описание", [])
        assert cat2.category_count == 2

    def test_product_counter(self):
        """Проверка счетчика продуктов"""
        assert Category.product_total == 0

        cat1 = Category("Кат 1", "Описание", ["Товар1", "Товар2"])
        assert cat1.product_count == 2

        cat2 = Category("Кат 2", "Описание", ["Товар3"])
        assert cat2.product_count == 3
