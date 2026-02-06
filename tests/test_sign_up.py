import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.main import MainPage
from pages.sign_up_page import Sign_Up

def test_sign_up(browser):
    m = MainPage(browser)
    m.open()
    print('Home page open')

    sup = Sign_Up(browser)
    sup.click_sign_up_button()
    print('Click sign up button')
    sup.perform_sign_up()

    # sup.close_window_su()

    print('Home page open')



    sup.click_log_in()
    print('Click log in button')
    sup.perform_login()


    if sup.get_welcome().text in "Welcome":
        print('Test success')

