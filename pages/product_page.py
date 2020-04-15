from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    @property
    def item_name_in_main(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_ITEM_NAME).text

    @property
    def item_price_in_main(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_ITEM_PRICE).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_successful_message(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_IN_SUCCESSFUL_ADD_MESSAGE),\
            "There is no successful add message for items to buy"
        assert self.is_element_present(*ProductPageLocators.TERMS_OF_OFFER_SUCCESSFUL_ADD_MESSAGE),\
            "There is no successful message for special terms of offer"
        assert self.is_element_present(*ProductPageLocators.TOTAL_BASKET_AMOUNT_SUCCESSFUL_ADD_MESSAGE),\
            "there is no successful message for total basket amount"

    def successful_message_should_be_right(self):
        item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_SUCCESSFUL_ADD_MESSAGE).text
        assert self.item_name_in_main == item_name_in_message, 'Item name in main and successful message does not equal'

        item_price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_SUCCESSFUL_TOTAL_BASKET_AMOUNT_MESSAGE).text
        navbar_text = self.browser.find_element(*ProductPageLocators.NAVBAR_BASKET_BUTTON)
        item_price_in_navbar = navbar_text.get_attribute('innerHTML').split(": ")[-1].rstrip()
        assert self.item_price_in_main == item_price_in_message, 'Item price in main and successful message does not equal'
        assert self.item_price_in_main == item_price_in_navbar, 'Item price in main and navbar does not equal'
