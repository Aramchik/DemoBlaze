from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
apple_monitor_24_name = (By.XPATH,"//*[text()='Apple monitor 24']")
apple_monitor_24_price = (By.XPATH,"//*[text()='$400']")
button_add_to_cart_apple_monitor_24 = (By.XPATH, "//a[@onclick='addToCart(10)']")


class Apple_monitor_24(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=10")


    # Getters
    def get_apple_monitor_24_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(apple_monitor_24_name))
    def get_apple_monitor_24_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(apple_monitor_24_price))
    def get_button_apple_monitor_24(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_apple_monitor_24))


    # Actions
    def click_apple_monitor_24(self):
        self.get_button_apple_monitor_24().click()