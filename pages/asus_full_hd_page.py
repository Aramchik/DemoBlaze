from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
asus_full_gd_name = (By.XPATH, "//*[text()='ASUS Full HD']")
asus_full_gd_price = (By.XPATH, "//*[text()='$230']")
button_add_to_cart_asus_full_hd = (By.XPATH, "//a[@onclick='addToCart(14)']")


class Asus_full_hd(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=14")


    # Getters
    def get_asus_full_hd_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(asus_full_gd_name))
    def get_asus_full_hd_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(asus_full_gd_price))
    def get_button_asus_full_hd(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_asus_full_hd))


    # Actions
    def click_asus_full_hd(self):
        self.get_button_asus_full_hd().click()