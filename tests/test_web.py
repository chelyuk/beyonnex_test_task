from src.pages.cart import CartPage
from src.pages.order import OrderPage
from src.pages.payment import PaymentWindow
from src.pages.weather_shopper import WeatherShopperPage
from src.pages.confirmation import ConfirmationPage


test_data = {
    "email": "someemail@google.com",
    "card_number": "4242 4242 4242 4242",
    "expiration_date": "10 / 2030",
    "CVV": "356",
    "zip_code": "18005",
}


def set_payment_details(window):
    window.set_email(test_data["email"])
    window.set_card(test_data["card_number"])
    window.set_expiration_date(test_data["expiration_date"])
    window.set_cvc(test_data["CVV"])
    window.set_zip_code(test_data["zip_code"])


def get_number_from_string(text):
    return int("".join(_ for _ in text if _.isdigit()))


def get_least_expensive_option(options):
    options_dict = {
        key: value
        for key, value in zip(
            options,
            [get_number_from_string(x.get_attribute(name="onclick")) for x in options],
        )
    }
    return min(options_dict, key=options_dict.get)


def test_logic(browser):
    shopper_page = WeatherShopperPage(browser)
    shopper_page.load()
    current_temperature = get_number_from_string(shopper_page.get_temperature())
    if current_temperature <= 19:
        shopper_page.go_for_moisturizers()
        attribute_1 = "Aloe"
        attribute_2 = "Almond"

    elif current_temperature >= 34:
        shopper_page.go_for_sunscreens()
        attribute_1 = "SPF-50"
        attribute_2 = "SPF-30"

    order_page = OrderPage(browser)
    first_item = get_least_expensive_option(
        order_page.get_buttons_with_attribute(attribute_1)
    )
    second_item = get_least_expensive_option(
        order_page.get_buttons_with_attribute(attribute_2)
    )
    first_item.click()
    second_item.click()
    order_page.go_to_cart()
    cart_page = CartPage(browser)
    assert sum(cart_page.get_price_per_item()) == get_number_from_string(
        cart_page.get_total_price()
    )
    cart_page.go_to_payment()
    payment_window = PaymentWindow(browser)
    set_payment_details(payment_window)
    payment_window.submit()
    confirmation_page = ConfirmationPage(browser)
    assert (
        confirmation_page.get_message()
        == "Your payment was successful. You should receive a follow-up call from our sales team."
    )

    print(first_item, second_item)
