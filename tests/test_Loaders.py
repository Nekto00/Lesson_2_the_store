import pytest
import json
from src.Loaders import JSONDataLoader


class TestJSONDataLoader:
    """Тесты для JSONDataLoader"""

    def test_file_loading(self, tmp_path):
        """Проверка загрузки данных из файла"""
        # Создаем временный файл для теста
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание",
                "products": [
                    {
                        "name": "Тестовый товар",
                        "description": "Описание товара",
                        "price": "100.0",
                        "quantity": "5"
                    }
                ]
            }
        ]

        file_path = tmp_path / "test_products.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)

        # Загружаем данные
        categories = JSONDataLoader.load_from_json(file_path)

        # Проверяем результаты
        assert len(categories) == 1
        assert categories[0].name == "Тестовая категория"
        assert len(categories[0].products) == 1
        assert categories[0].products[0].name == "Тестовый товар"
        assert categories[0].products[0].price == 100.0
        assert categories[0].products[0].quantity == 5

    def test_file_not_found(self):
        """Проверка обработки отсутствующего файла"""
        with pytest.raises(FileNotFoundError):
            JSONDataLoader.load_from_json("nonexistent_file.json")

    def test_invalid_json(self, tmp_path):
        """Проверка обработки некорректного JSON"""
        file_path = tmp_path / "invalid.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("{invalid json}")

        with pytest.raises(json.JSONDecodeError):
            JSONDataLoader.load_from_json(file_path)