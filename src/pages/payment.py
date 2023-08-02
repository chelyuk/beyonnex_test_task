from selenium.webdriver.common.by import By

from src.pages.base import BasePage


class PaymentWindow(BasePage):
    EMAIL_FIELD = "email"
    CARD_NUMBER_FIELD = "card_number"
    EXPIRATION_DATE_FIELD = "cc-exp"
    CVC_FIELD = "cc-csc"
    ZIP_CODE_FIELD = "billing-zip"
    SUBMIT_BUTTON = (By.ID, "submitButton")

    def __init__(self, browser):
        super().__init__(browser)
        browser.switch_to.frame(
            browser.find_element(By.CLASS_NAME, "stripe_checkout_app")
        )

    def set_text(self, element, text):
        field = self.browser.find_element(By.ID, element)
        for i in text:
            field.send_keys(i)

    def set_email(self, text):
        self.set_text(self.EMAIL_FIELD, text)

    def set_card(self, text):
        self.set_text(self.CARD_NUMBER_FIELD, text)

    def set_expiration_date(self, text):
        self.set_text(self.EXPIRATION_DATE_FIELD, text)

    def set_cvc(self, text):
        self.set_text(self.CVC_FIELD, text)

    def set_zip_code(self, text):
        self.set_text(self.ZIP_CODE_FIELD, text)

    def submit(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()
        return self.browser.switch_to.default_content()
