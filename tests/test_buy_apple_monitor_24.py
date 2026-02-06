import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.cart_page import Cart_page
from pages.main import MainPage
from pages.apple_monitor_24_page import Apple_monitor_24

def test_buy_apple_monitor_24(browser):
    m = MainPage(browser)
    m.open()
    m.click_monitor_category()
    print("Click Monitors")
    m.click_apple_monitor_24()
    print("Click Apple monitor 24")

    am24 = Apple_monitor_24(browser)
    am24.click_apple_monitor_24()
    print("Click add to cart")

    m.click_cart()
    print('Click cart')

    m.assert_values(word=am24.get_apple_monitor_24_name(), result="Apple monitor 24")
    print('Name good')

    price_400 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '400')]")
    m.assert_values(price_400, "400")
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




