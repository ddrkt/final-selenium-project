from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('offer_id', ['0', '1', '2', '3', '4', '5', '6',
                                      pytest.param('7', marks=pytest.mark.xfail),
                                      '8', '9'])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successful_message()
    page.successful_message_should_be_right()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_successful_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_successful_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_successful_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_content()
    basket_page.should_be_empty_basket_content()
    basket_page.should_not_be_basket_summary()
    basket_page.should_be_disappeared_basket_summary()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        self.browser = browser

        page = LoginPage(self.browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, 'asd123zxcff')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_successful_message()

    def test_user_can_add_product_to_basket(self):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_successful_message()
        page.successful_message_should_be_right()
