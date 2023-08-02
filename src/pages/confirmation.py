from selenium.webdriver.common.by import By

from src.pages.base import BasePage


class ConfirmationPage(BasePage):

    MESSAGE = (By.CLASS_NAME, "text-justify")

    def get_message(self):
        return self.browser.find_element(*self.MESSAGE).text
