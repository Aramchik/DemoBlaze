import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage
from pages.main import MainPage
from pages.samsung_galaxy_s7_page import Samsung_s7_Page
from pages.cart_page import Cart_page

def test_buy_sgs7(browser):
    m = MainPage(browser)
    m.open()
    m.click_sgs7()
    print("Click Samsung galaxy s7")

    sgs7 = Samsung_s7_Page(browser)
    sgs7.click_sgs7()
    print("Click add to cart")

    m.click_cart()
    print('Click cart')

    m.assert_values(word=sgs7.get_name_s7(), result="Samsung galaxy s7")
    print('Name good')

    price_800 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '800')]")
    m.assert_values(price_800, "800")
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




