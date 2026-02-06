from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
button_add_to_cart_iphone6_32 = (By.XPATH, "//a[@onclick='addToCart(5)']")
iphone_name = (By.XPATH, "//*[text()='Iphone 6 32gb']")
iphone_price = (By.XPATH, "//*text()='$790']")


class Iphone6_32_Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=4")


    # Getters
    def get_iphone_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(iphone_name))
    def get_iphone_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(iphone_price))
    def get_button_iphone6_32(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_iphone6_32))


    # Actions
    def click_iphone6_32(self):
        self.get_button_iphone6_32().click()