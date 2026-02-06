import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import pytest
from faker import Faker



class BasePage:
    # our browser and faker
    def __init__(self, browser):
        self.browser = browser
        self.fake = Faker()
        self.name = self.fake.first_name_male()
        self.country = self.fake.country()
        self.city = self.fake.city()
        self.credit_card = self.fake.credit_card_number()
        self.month = self.fake.month()
        self.year = self.fake.year()

        self.credentials = {
            "username": self.fake.user_name(),
            "password": self.fake.password(),

        }

    # function for assert
    def assert_values(self, word, result):
        value_word = word.text
        assert value_word == result

    # function for go back
    def go_back(self):
        for _ in range(2):
            self.browser.back()


    # function for log in
    def login_with_faker(self, browser):
        self.username = self.fake.user_name()
        self.password = self.fake.password()

        browser.username = self.username  # Сохраняем в объекте browser как атрибут
        browser.password = self.password

    def get_credentials(self):
        return self.credentials
