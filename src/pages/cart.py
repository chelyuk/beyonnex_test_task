from selenium.webdriver.common.by import By

from src.pages.base import BasePage


class CartPage(BasePage):

    ITEM_PRICE = (By.XPATH, "//td/following-sibling::td")
    TOTAL_PRICE = (By.ID, "total")
    PAY_BUTTON = (By.CLASS_NAME, "stripe-button-el")

    def get_price_per_item(self):
        return [int(_.text) for _ in self.browser.find_elements(*self.ITEM_PRICE)]

    def get_total_price(self):
        return self.browser.find_element(*self.TOTAL_PRICE).text

    def go_to_payment(self):
        return self.browser.find_element(*self.PAY_BUTTON).click()
