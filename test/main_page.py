from playwright.sync_api import Page, Locator, expect

class MainPage():
    def __init__(self, page:Page):
        self.page = page
        
        self.min_price_input: Locator = page.get_by_placeholder("От")
        self.max_price_input: Locator = page.get_by_placeholder("До")
        self.category_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Категория') + select._filters__select_1iunh_21")
        self.sorting_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Сортировать по') + select._filters__select_1iunh_21")
        self.order_select: Locator = page.locator("label._filters__label_1iunh_8:has-text('Порядок') + select._filters__select_1iunh_21")
        self.urgent_toggle: Locator = page.get_by_role('checkbox')
        
        self.announcement_cards: Locator = page.locator("div[class^='_card_']")
        self.price_of_elements: Locator = page.locator(".div[class^='_card__price_']")
        self.category_of_elements: Locator = page.locator("div[class^='_card__category_']")
        
    def goto(self):
        self.page.goto("https://cerulean-praline-8e5aa6.netlify.app/")
            
    def apply_price_filter(self, min_price:int, max_price:int):
        self.min_price_input.fill(str(min_price))
        self.max_price_input.fill(str(max_price))
        
        self.page.keyboard.press("Enter")
        self.price_of_elements.first.wait_for(state="visible", timeout=12000)
    
    def sort_by_price(self, order: str = "asc"):    
        self.sorting_select.select_option(label="Цене")
        
        if order.lower() == "asc":
            self.order_select.select_option(label='По возрастанию')
        else:
            self.order_select.select_option(label='По убыванию')
            
        self.price_of_elements.first.wait_for(state="visible", timeout=12000)
        
    def toggle_urgent_only(self, enable:bool):
        pass
    
    def get_price_of_items(self):
        
        texts = self.price_of_elements.all_text_contents()
        
        list_price = []
        for text in texts:
            clean = ''.join(filter(str.isdigit, text.replace(" ", "").replace("₽", "")))
            if clean:
                list_price.append(float(clean))
        
        return list_price
    
    def get_category_of_items(self):
        category = self.category_of_elements.all_text_contents()
        
        return category
            
    def set_category(self, label):
        self.category_select.select_option(label=label)

        self.announcement_cards.first.wait_for(state="visible", timeout=11000)