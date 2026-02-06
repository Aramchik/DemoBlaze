from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
button_add_to_cart_samsung_s7 = (By.XPATH, "//a[@onclick='addToCart(4)']")

samsung_s7_name = (By.XPATH, "//*[text()='Samsung galaxy s7']")
samsung_s7_price = (By.XPATH, "//*[text()='$800']")


class Samsung_s7_Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=4")


    # Getters
    def get_name_s7(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(samsung_s7_name))
    def get_price_s7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(samsung_s7_price))
    def get_button_sgs7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_samsung_s7))


    # Actions
    def click_sgs7(self):
        self.get_button_sgs7().click()