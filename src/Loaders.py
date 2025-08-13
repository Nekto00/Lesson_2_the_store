import json
from typing import List
from src.Category import Category
from src.Product import Product

class JSONDataLoader:
    """Класс для загрузки данных из JSON файла"""

    @staticmethod
    def load_from_json(file_path: str) -> List[Category]:
        """
        Загружает данные из JSON файла и создает объекты Category и Product

        :param file_path: путь к JSON файлу
        :return: список объектов Category
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        categories = []

        for category_data in data:
            # Создаем продукты для категории
            products = []
            for product_data in category_data['products']:
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=float(product_data['price']),
                    quantity=int(product_data['quantity'])
                )
                products.append(product)

            # Создаем категорию
            category = Category(
                name=category_data['name'],
                description=category_data['description'],
                products=products
            )
            categories.append(category)

        return categories
