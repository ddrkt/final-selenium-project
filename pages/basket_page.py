from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_login_page(self):
        self.should_be_basket_url()
        self.should_be_basket_content()

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, "'Url does not contain '/basket'"

    def should_be_basket_content(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), "Basket content does not present"

    def should_be_empty_basket_content(self):
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert 'basket is empty' in basket_content, 'Basket content does not empty'

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY),\
                "Basket summary is present, but it should not be"

    def should_be_disappeared_basket_summary(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_SUMMARY),\
                "Basket summary does not disappeared"
