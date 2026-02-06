import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage
from pages.main import MainPage
from pages.iphone6_32_page import Iphone6_32_Page
from pages.cart_page import Cart_page

def test_buy_iphone6_32(browser):
    m = MainPage(browser)
    m.open()
    m.click_iphone6_32()
    print("Click Iphone 6 32gb")

    i632 = Iphone6_32_Page(browser)
    i632.click_iphone6_32()
    print("Click add to cart")

    m.click_cart()
    print('Click cart')

    m.assert_values(word=i632.get_iphone_name(), result="Iphone 6 32gb")
    print('Name good')

    price_790 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '790')]")
    m.assert_values(price_790, "790")
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






