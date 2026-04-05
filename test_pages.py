import pytest
from page import MainPage, StatPage
from playwright.sync_api import Page, Locator, expect, sync_playwright



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
        assert card.locator("div[class^='_card__priority_']").count() > 0, "переключатель 'Только Cрочные' не работает"


def test_refresh_time(page):
    stat_page = StatPage(page)
    stat_page.goto()
    #Проверку на до и после по времени
    stat_page.refresh_timer()
    after_time = stat_page.get_time()
    
    assert after_time == "5:00", "Обновление таймера не работает"
    

def test_pause_time(page):
    stat_page = StatPage(page)
    stat_page.goto()
    stat_page.pause_timer()
    
    assert stat_page.disabled_text.is_visible(), "Кнопка паузы не работает" 
    
def test_start_time(page):
    stat_page = StatPage(page)
    stat_page.goto()
    stat_page.pause_timer()
    stat_page.start_timer()
    
    assert stat_page.disabled_text.is_visible() == False, "Кнопка старта не работает"

def test_theme_switch_on_mobile(playwright, page):
    iphone_12 = playwright.devices['iPhone 12']
    
    context = page.context.browser.new_context(**iphone_12)
    mobile_page = context.new_page()
    
    try:
        main_page = MainPage(mobile_page)
        main_page.goto()

        initial_theme = main_page.get_theme()

        main_page.switch_theme()
        mobile_page.wait_for_timeout(800)
        theme_after_first = main_page.get_theme()

        assert theme_after_first != initial_theme, "Переключение со светлой на тёмную не работает"

        main_page.switch_theme()
        mobile_page.wait_for_timeout(800)
        theme_after_second = main_page.get_theme()

        assert theme_after_second == initial_theme, "Переключение с тёмной на светлую не работает"

    finally:
        context.close()