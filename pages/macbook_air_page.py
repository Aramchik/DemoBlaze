from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
macbook_air_name = (By.XPATH, "//*[text()='MacBook air']")
macbook_air_price = (By.XPATH, "//*[text()='$700']")
button_add_to_cart_macbook_air = (By.XPATH, "//a[@onclick='addToCart(11)']")


class Macbook_air(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=11")


    # Getters
    def get_macbook_air_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(macbook_air_name))
    def get_macbook_air_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(macbook_air_price))
    def get_button_macbook_air(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_macbook_air))


    # Actions
    def click_macbook_air(self):
        self.get_button_macbook_air().click()