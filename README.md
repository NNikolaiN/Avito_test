# Avito Test — UI автотесты

Автоматизированные UI-тесты для демо-приложения.
Стек: Playwright + pytest (Python).

### Стуктура проекта

```
├── pages.py          # Page Object модели
├── test_pages.py     # UI тесты
├── TESTCASES.md      # Тест-кейсы
├── BUGS.md           # Найденные баги
├── requirements.txt
└── README.md
```

### Требования

**Перед запуском убедись, что установлено:**

- Python 3.10+
- Git

**Проверка:**
```bash
python --version
git --version
```
## Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/NNikolaiN/Avito_test
cd Avito_test
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```
### 4. Установка браузеров
```bash
playwright install
```

### 5. Запуск тестов
```bash
pytest -v
```

## ТЕСТ-КЕЙС

TESTCASES.md

## Баги

BUGS.md