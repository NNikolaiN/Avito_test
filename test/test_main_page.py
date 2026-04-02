from main_page import MainPage
from playwright.sync_api import Page, Locator, expect


# Тестирование фильтра "Диапазон цен"
def test_filter_price(page):
    main_page = MainPage(page)
    main_page.goto()
    main_page.apply_price_filter(1000,3000)
    
    prices = main_page.get_price_of_items()
    
    assert len(prices) > 0
    assert all(1000 <= p <= 3000 for p in prices), "Фильтр цены не работает"

# Тестироание сортировки "По цене"
def test_sort_by_price(page):
    main_page = MainPage(page)
    main_page.goto()
    
    main_page.sort_by_price()
    price = main_page.get_price_of_items()
    
    assert price == sorted(price, reverse=True), "Сортировка по цене не работает корректно"