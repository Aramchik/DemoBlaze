import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.main import MainPage
from pages.sign_up_page import Sign_Up

def test_log_in(browser):
    m = MainPage(browser)
    m.open()
    print('Home page open')

    sup = Sign_Up(browser)
    sup.click_log_in()
    print('Click log in button')
    sup.get_user_name_li().send_keys('admin')
    sup.get_password_li().send_keys('admin')
    sup.click_log_in_window()
    print('Home page open')

    sup.assert_welcome()