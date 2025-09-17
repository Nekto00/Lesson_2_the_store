import pytest

from src.Category import Category
from src.Product import LawnGrass, Product, Smartphone


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
        with pytest.raises(TypeError) as exc_info:
            category.add_product(invalid_product)

        # Дополнительная проверка сообщения об ошибке
        assert "Можно добавлять только объекты класса Product или его наследников" in str(exc_info.value)
        assert len(category.products) == 0
        assert category.product_count == 0

    def test_add_valid_product(self, category):
        """Тест добавления валидного продукта"""
        product = Product("Ноутбук", "Игровой ноутбук", 50000.0, 5)
        initial_count = Category.product_total

        category.add_product(product)

        assert len(category.products) == 1
        assert Category.product_total == initial_count + 1
        assert category.products[0].name == "Ноутбук"

    def test_add_smartphone(self, category):
        """Тест добавления смартфона"""
        smartphone = Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий")
        initial_count = Category.product_total

        category.add_product(smartphone)

        assert len(category.products) == 1
        assert Category.product_total == initial_count + 1
        assert isinstance(category.products[0], Smartphone)

    def test_add_lawn_grass(self, category):
        """Тест добавления газонной травы"""
        grass = LawnGrass("Трава", "Газонная", 1500.0, 10, "Россия", 14, "Зеленый")
        initial_count = Category.product_total

        category.add_product(grass)

        assert len(category.products) == 1
        assert Category.product_total == initial_count + 1
        assert isinstance(category.products[0], LawnGrass)

    def test_add_invalid_object_error(self, category):
        """Тест ошибки при добавлении невалидного объекта"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product("не продукт")

    def test_add_number_error(self, category):
        """Тест ошибки при добавлении числа"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product(123)

    def test_add_list_error(self, category):
        """Тест ошибки при добавлении списка"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product([1, 2, 3])

    def test_add_dict_error(self, category):
        """Тест ошибки при добавлении словаря"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product({"name": "product"})

    def test_add_none_error(self, category):
        """Тест ошибки при добавлении None"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product(None)

    def test_add_product_type_check(self, category):
        """Тест проверки типа добавляемого продукта"""
        # Должно работать
        product = Product("Тест", "Тестовый", 1000, 1)
        category.add_product(product)

        # Должно вызывать ошибку
        with pytest.raises(TypeError):
            category.add_product("invalid")

    def test_add_multiple_products(self, category):
        """Тест добавления нескольких продуктов"""
        products = [
            Product("Ноутбук", "Игровой ноутбук", 50000.0, 5),
            Smartphone("iPhone", "Смартфон", 90000.0, 3, 95.5, "15 Pro", 256, "Синий"),
            LawnGrass("Трава", "Газонная", 1500.0, 10, "Россия", 14, "Зеленый")
        ]

        initial_count = Category.product_total

        for product in products:
            category.add_product(product)

        assert len(category.products) == 3
        assert Category.product_total == initial_count + 3


@pytest.fixture
def category():
    """Фикстура для создания категории с пустым списком продуктов"""
    return Category("Электроника", "Техника", [])
