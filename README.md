# Avito Test (UI Автотесты)

Тестовое задание для стажировки Авито — автоматизированные UI-тесты на Playwright + pytest.

## Что проверяется

- Фильтр по диапазону цен
- Сортировка по цене (по возрастанию и убыванию)
- Фильтр по категориям
- Тоггл «Только срочные»
- Работа таймера на странице статистики
- Переключение темы (мобильная версия)

## Технологии

- Python 3.10+
- Playwright
- pytest + pytest-playwright

## Требования

- Установлен **Python 3.10** или выше
- Установлен **Git**

## Быстрый запуск (рекомендуемый способ)

### 1. Клонировать репозиторий

```bash
git clone <URL_вашего_репозитория>
cd Avito_test
2. Создать и активировать виртуальное окружение
Bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Установить зависимости
Bashpip install -r requirements.txt
4. Установить браузеры Playwright
Bashplaywright install chromium --with-deps
5. Запустить все тесты
Bashpytest -v
Полезные команды
Bash# Запуск только десктопных тестов
pytest -v -k "not mobile"

# Запуск тестов с отчётом в HTML
pytest --html=report.html --self-contained-html

# Запуск с показом браузера (headful)
pytest --headed

# Запуск конкретного теста
pytest -v test_pages.py::test_filter_price
Структура проекта
textAvito_test/
├── pages.py              # Page Object модели
├── test_pages.py         # Все автотесты
├── TESTCASES.md          # Тест-кейсы
├── BUGS.md               # Найденные баги
├── requirements.txt
└── README.md
Примечания

Тесты запускаются против демо-приложения: https://cerulean-praline-8e5aa6.netlify.app/
Для мобильного теста используется эмуляция iPhone 12
Все критичные баги (P0) из BUGS.md воспроизводятся тестами