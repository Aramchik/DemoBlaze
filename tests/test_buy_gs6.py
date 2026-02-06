import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.main import MainPage
from pages.Samsung_galaxy_s6_page import Samsung_s6_Page
from pages.cart_page import Cart_page


# Test buy Samsung galaxy s6
def test_buy_sgs6(browser):
    # variable m is an object of the class Main
    m = MainPage(browser)
    m.open()
    m.click_sgs6()
    print('Click Samsung galaxy s6')

    # variable bsgls6 is an object of the class Samsung_s6_Page
    bsgls6 = Samsung_s6_Page(browser)
    bsgls6.click_sgs6()
    print('Click btn add to cart')

    m.click_cart()
    print('Click cart')


    m.assert_values(word=bsgls6.get_samsung_name(), result="Samsung galaxy s6")
    print('Name good')


    price_360 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '360')]")
    m.assert_values(price_360, "360")
    print('Price good')


    # variable cp is an object of the class Cart_page
    cp = Cart_page(browser)
    cp.click_order_button()
    print('Click Place Order')

    cp.send_info()

    cp.click_purchase()
    print('Click Purchase')


    m.assert_values(cp.get_success_text(),'Thank you for your purchase!')
    print('Success text good')


    time.sleep(1)

    cp.click_ok()
    print('Click ok')

    WebDriverWait(browser, 15).until(Ec.url_to_be("https://www.demoblaze.com/index.html"))
    assert browser.current_url == "https://www.demoblaze.com/index.html"
    print('Home page')
