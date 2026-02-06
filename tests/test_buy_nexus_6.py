import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.main import MainPage
from pages.nexus_6_page import Nexus_page
from pages.cart_page import Cart_page


# Test buy Nexus 6
def test_buy_nexus(browser):
    m = MainPage(browser)
    m.open()
    m.click_nexus()
    print("Click Nexus 6")



    n6 = Nexus_page(browser)
    n6.click_nexus()
    print("Click btn add to cart")



    m.click_cart()
    print('Click cart')

    m.assert_values(word=n6.get_nexus_name(), result="Nexus 6")
    print('Name good')

    price_650 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '650')]")
    m.assert_values(price_650, "650")
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

