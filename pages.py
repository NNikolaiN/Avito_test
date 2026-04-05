from playwright.sync_api import Page, Locator, expect

class MainPage():
    def __init__(self, page:Page):
        self.page = page
        
        self.min_price_input: Locator = page.get_by_placeholder("От")
        self.max_price_input: Locator = page.get_by_placeholder("До")
        self.category_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Категория') + select._filters__select_1iunh_21")
        self.sorting_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Сортировать по') + select._filters__select_1iunh_21")
        self.order_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Порядок') + select._filters__select_1iunh_21")
        self.urgent_toggle: Locator = page.locator("label._urgentToggle_h1vv9_1")
        self.swich_theme_button: Locator = page.locator("._themeToggle_127us_1")
        
        self.theme_style_text: Locator = page.locator("._label_127us_35")
        self.announcement_cards: Locator = page.locator("div[class^='_card_']")
        self.price_of_elements: Locator = page.locator("div[class^='_card__price_']")
        self.category_of_elements: Locator = page.locator("div[class^='_card__category_']")
        self.urgent_mod_of_elements: Locator = page.locator("div[class^='_card__priority_']")
        
    def goto(self):
        self.page.goto("https://cerulean-praline-8e5aa6.netlify.app/")
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
            
    def apply_price_filter(self, min_price:int, max_price:int):
        
        self.min_price_input.clear()
        self.max_price_input.clear()
        
        self.min_price_input.fill(str(min_price))
        self.max_price_input.fill(str(max_price))
    
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
        
    def sort_by_price(self, order: str = "asc"):    
        self.sorting_select.select_option(label="Цене")
        
        if order.lower() == "asc":
            self.order_select.select_option(label='По возрастанию')
        else:
            self.order_select.select_option(label='По убыванию')
        
        self.page.wait_for_timeout(1000)    
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
        
    def get_price_of_items(self):
        
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
        
        texts = self.price_of_elements.all_text_contents()
        list_price = []
        
        for text in texts:
            clean = ''.join(filter(str.isdigit, text.replace(" ", "").replace("₽", "")))
            if clean:
                list_price.append(float(clean))
        
        return list_price
    
    def get_category_of_items(self):
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
        category = self.category_of_elements.all_text_contents()
        
        return category
            
    def set_category(self, label):
        self.category_select.select_option(label=label)
        self.page.wait_for_timeout(1000)
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
    
    def set_urgent_toogle(self):
        self.urgent_toggle.click()
        self.page.wait_for_timeout(1000)
        self.announcement_cards.first.wait_for(state="visible", timeout=12000)
        
    def get_item(self):
        all_cards = self.announcement_cards.all()
        
        return all_cards
    
    def switch_theme(self):
        self.swich_theme_button.click()
    
    def get_theme(self):
        return self.theme_style_text.text_content()

class StatPage():
    def __init__(self, page:Page):
        self.page = page
        
        
        self.refresh_button: Locator = page.locator('._refreshButton_ir5wu_16')
        self.toggle_button_pause: Locator = page.locator('._toggleButton_ir5wu_69._toggleButton_active_ir5wu_89')
        self.toggle_button_start: Locator = page.locator('button[title="Включить автообновление"]')
        
        self.stat_page: Locator = page.get_by_role('link', name='Статистика')
        self.time_value: Locator = page.locator("._timeValue_ir5wu_112")
        self.disabled_text: Locator = page.locator('text="Автообновление выключено"')
    
    def goto(self):
        self.page.goto("https://cerulean-praline-8e5aa6.netlify.app/")
        self.stat_page.click()
        self.page.wait_for_timeout(5000)
    
    def get_time(self):
        self.time_value.wait_for(state="visible", timeout=3000)
        return self.time_value.text_content()
    
    def refresh_timer(self):
        self.refresh_button.click()
        
    def pause_timer(self):
        self.toggle_button_pause.click()
    
    def start_timer(self):
        self.toggle_button_start.click()