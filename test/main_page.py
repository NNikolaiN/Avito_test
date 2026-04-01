from playwright.sync_api import Page, Locator, expect

class MainPage():
    def __init__(self, page:Page):
        self.page = page
        
        self.min_price_input: Locator = page.get_by_placeholder("От")
        self.max_price_input: Locator = page.get_by_placeholder("До")
        self.filter_select: Locator = page.locator("_filters__select_1iunh_21")
        self.sorted_select: Locator = page.locator("_filters__select_1iunh_21")
        self.urgent_toggle: Locator = page.get_by_role('checkbox')
        
        self.announcement_cards: Locator = page.locator(".card_15fhn_2")
        self.price_elements: Locator = page.locator("._card__price_15fhn_241")
        
    def goto(self):
        self.page.goto("https://cerulean-praline-8e5aa6.netlify.app/")
            
    def apply_price_filter(self, min_price:int, max_price:int):
        self.min_price_input.fill(str(min_price))
        self.max_price_input.fill(str(max_price))
        
    def toggle_urgent_only(self, enable:bool):
        pass
    
    def get_price_of_items(self):
        self.price_elements.first.wait_for(state="visible", timeout=10000)
        prices = self.price_elements.all_text_contents()
        
        list_price = []
        
        for i in prices:
            clean_price = ''.join(filter(str.isdigit, i.replace(" ", "").replace("₽", "")))
            list_price.append(float(clean_price))
        return list_price