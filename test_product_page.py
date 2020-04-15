from pages.product_page import ProductPage
import pytest


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

