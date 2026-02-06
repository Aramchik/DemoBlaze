import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import pytest

from pages.cart_page import Cart_page
from pages.main import MainPage
from pages.nokia_lumia_page import Nokia_Lumia_Page

# Test buy Nokia Lumia 1520
def test_buy_nokia(browser):
    # variable m is an object of the class Main
    m = MainPage(browser)
    m.open()
    m.click_nokia()
    print('Click Nokia Lumia 1520')

    nl1520 = Nokia_Lumia_Page(browser)
    nl1520.click_nokia()
    print('Click btn add to cart')

    m.click_cart()
    print('Click cart')

    m.assert_values(word=nl1520.get_nokia_name(), result="Nokia lumia 1520")
    print('Name good')

    price_820 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '820')]")
    m.assert_values(price_820, "820")
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



    WebDriverWait(browser,15).until(Ec.url_to_be("https://www.demoblaze.com/index.html"))
    assert browser.current_url == "https://www.demoblaze.com/index.html"
    print('Home page')

