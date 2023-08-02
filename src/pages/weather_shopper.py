from selenium.webdriver.common.by import By

from src.pages.base import BasePage


class WeatherShopperPage(BasePage):
    URL = "https://weathershopper.pythonanywhere.com/"
    TEMPERATURE_VALUE = (By.ID, "temperature")
    MOISTURIZERS = (By.XPATH, "//button[text()='Buy moisturizers']")
    SUNSCREENS = (By.XPATH, "//button[text()='Buy sunscreens']")

    def load(self):
        self.browser.get(self.URL)

    def get_temperature(self):
        return self.browser.find_element(*self.TEMPERATURE_VALUE).text

    def go_for_moisturizers(self):
        return self.browser.find_element(*self.MOISTURIZERS).click()

    def go_for_sunscreens(self):
        return self.browser.find_element(*self.SUNSCREENS).click()
