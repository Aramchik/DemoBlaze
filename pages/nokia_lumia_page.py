from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage


# Lockator
button_add_to_cart_nokia = (By.XPATH, "//a[@onclick='addToCart(2)']")
nokia_lumia_name = (By.XPATH, "//*[text()='Nokia lumia 1520']")
nokia_lumia_price = (By.XPATH, "//*[text()='$820']")


class Nokia_Lumia_Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=2")



    # Getters
    def get_button_nokia(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_nokia))


    def get_nokia_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(nokia_lumia_name))

    def get_nokia_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(nokia_lumia_price))

    # Actions
    def click_nokia(self):
        self.get_button_nokia().click()