from selenium.webdriver.common.by import By

from src.pages.base import BasePage


class OrderPage(BasePage):

    MOISTURIZERS = (By.CSS_SELECTOR, ".font-weight-bold.top-space-10")
    BUTTONS = (By.CSS_SELECTOR, ".btn.btn-primary")
    CART_BUTTON = (By.CSS_SELECTOR, ".thin-text.nav-link")

    def get_moisturizers(self):
        return self.browser.find_elements(*self.MOISTURIZERS)

    def get_buttons(self):
        return self.browser.find_elements(*self.BUTTONS)

    def find_the_least_expensive_moisture(self):
        pass

    def get_moistures_with_attribute(self, attribute):
        return [x for x in self.get_moisturizers() if attribute in x.text]

    def get_buttons_with_attribute(self, attribute):
        return [
            x
            for x in self.get_buttons()
            if attribute in x.get_attribute(name="onclick")
        ]

    def go_to_cart(self):
        return self.browser.find_element(*self.CART_BUTTON).click()
