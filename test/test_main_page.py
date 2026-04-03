import pytest
from main_page import MainPage
from playwright.sync_api import Page, Locator, expect


# Тестирование фильтра "Диапазон цен"
@pytest.mark.parametrize("min_price, max_price", [
    (0, 1000),
    (1000, 3000),
    (3000, 10000),
    (10000, 100000),
])
def test_filter_price(page, min_price, max_price):
    main_page = MainPage(page)
    main_page.goto()

    main_page.apply_price_filter(min_price, max_price)
    prices = main_page.get_price_of_items()

    assert len(prices) > 0, "Нет объявлений"
    assert all(min_price <= p <= max_price for p in prices), \
        f"Фильтр не работает для диапазона {min_price}-{max_price}"
        
# Тестироание сортировки "По цене"
def test_sort_by_price(page):
    main_page = MainPage(page)
    main_page.goto()
    
    main_page.sort_by_price()
    price = main_page.get_price_of_items()
    
    assert price == sorted(price) , "Сортировка по цене не работает корректно"
    
def test_sort_by_price_desc(page):
    main_page = MainPage(page)
    main_page.goto()
    
    main_page.sort_by_price(order="desc")
    price = main_page.get_price_of_items()
    
    assert price == sorted(price, reverse=True), "Сортировка по цене не работает корректно"

# Тестирование категорий
@pytest.mark.parametrize("category", [
    "Недвижимость",
    "Электроника",
    "Транспорт",
    "Работа",
    "Услуги",
    "Животные",
    "Мода",
    "Детское"
])
def test_categories(page, category):
    main_page = MainPage(page)
    main_page.goto()
    
    main_page.set_category(label=category)
    cat_of_items = main_page.get_category_of_items()
    
    assert len(cat_of_items) > 0, "Нет объявлений"
    assert all(cat == category for cat in cat_of_items), f"Категория {category} работает некорректно"

def test_urgent_mod(page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.set_urgent_toogle()
    
    cards = main_page.get_item()
    
    for card in cards:
        assert card.locator("div[class^='_card__priority_']").count() > 0
    