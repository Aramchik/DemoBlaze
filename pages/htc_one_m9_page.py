from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
htc_name = (By.XPATH, "//*[text()='HTC One M9']")
htc_price = (By.XPATH, "//*[text()='$700']")
button_add_to_cart_htc_one_m9 = (By.XPATH, "//a[@onclick='addToCart(7)']")


class Htc_one_m9(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=7")


    # Getters
    def get_htc_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(htc_name))
    def get_htc_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(htc_price))
    def get_button_htc(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_htc_one_m9))


    # Actions
    def click_htc(self):
        self.get_button_htc().click()