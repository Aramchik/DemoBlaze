import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.cart_page import Cart_page
from pages.main import MainPage
from pages.macbook_pro_page import Macbook_pro

def test_buy_macbook_pro(browser):
    m = MainPage(browser)
    m.open()
    m.click_laptops()
    print("Click Laptops")
    m.click_macbook_pro()
    print("Click Macbook pro")

    mbpro = Macbook_pro(browser)
    mbpro.click_macbook_pro()
    print("Click add to cart")

    m.click_cart()
    print('Click cart')

    m.assert_values(word=mbpro.get_macbook_pro_name(), result="MacBook Pro")
    print('Name good')

    price_1100 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '1100')]")
    m.assert_values(price_1100, "1100")
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




