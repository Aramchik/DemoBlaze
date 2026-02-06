from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
macbook_pro_name = (By.XPATH, "//*[text()='MacBook Pro']")
macbook_pro_price = (By.XPATH, "//*[text()='$1100']")
button_add_to_cart_macbook_pro = (By.XPATH, "//a[@onclick='addToCart(15)']")


class Macbook_pro(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=15")


    # Getters
    def get_macbook_pro_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(macbook_pro_name))
    def get_macbook_pro_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(macbook_pro_price))
    def get_button_macbook_pro(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_macbook_pro))


    # Actions
    def click_macbook_pro(self):
        self.get_button_macbook_pro().click()