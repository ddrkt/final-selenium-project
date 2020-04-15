from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ITEM_IN_SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner")
    TERMS_OF_OFFER_SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(2) .alertinner")
    TOTAL_BASKET_AMOUNT_SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR,
                                                  "#messages > div:nth-child(3) .alertinner p:first-child")
    ITEM_NAME_IN_SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    PRICE_IN_SUCCESSFUL_TOTAL_BASKET_AMOUNT_MESSAGE = (By.CSS_SELECTOR,
                                                  "#messages > div:nth-child(3) .alertinner p:first-child strong")
    MAIN_ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MAIN_ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p:nth-child(2)")
    NAVBAR_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-cart")


class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#basket_formset")
