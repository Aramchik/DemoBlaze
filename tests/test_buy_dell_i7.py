import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.main import MainPage
from pages.dell_i7_page import Dell_i7
from pages.cart_page import Cart_page

def test_buy_dell_i7(browser):
    m = MainPage(browser)
    m.open()
    m.click_laptops()
    print("Click Laptops")
    m.click_dell_i7()
    print("Click Dell i7 8gb")

    delli7 = Dell_i7(browser)
    delli7.click_dell_i7()
    print("Click add to cart")

    m.click_cart()
    print('Click cart')

    m.assert_values(word=delli7.get_dell_i7_name(), result="Dell i7 8gb")
    print('Name good')

    price_700 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '700')]")
    m.assert_values(price_700, "700")
    print('Price good')

    # variable cp is an object of the class Cart_page
    cp = Cart_page(browser)
    cp.click_order_button()
    print('Click Place Order')

    cp.send_info()

    cp.click_purchase()
    print('Click Purchase')

    m.assert_values(cp.get_success_text(), 'Thank you for your purchase!')
    print('Success text good')

    time.sleep(1)

    cp.click_ok()
    print('Click ok')

    WebDriverWait(browser, 15).until(Ec.url_to_be("https://www.demoblaze.com/index.html"))
    assert browser.current_url == "https://www.demoblaze.com/index.html"
    print('Home page')




