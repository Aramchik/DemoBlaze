from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
button_add_to_cart_sony_xperia_z5 = (By.XPATH, "//a[@onclick='addToCart(6)']")
sony_xperia_name = (By.XPATH, "//*[text()='Sony xperia z5']")
sony_xperia_price = (By.XPATH, "//*[text()='$320']")


class Sony_xperia_z5(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=6")


    # Getters
    def get_sony_xperia_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_xperia_name))
    def get_sony_xperia_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_xperia_price))
    def get_button_sxz5(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_sony_xperia_z5))


    # Actions
    def click_sxz5(self):
        self.get_button_sxz5().click()