from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
dell_i7_name = (By.XPATH, "//*[text()='Dell i7 8gb']")
dell_i7_price = (By.XPATH, "//*[@id='tbodyid']/div[4]/div/div/h5")
button_add_to_cart_dell_i7 = (By.XPATH, "//a[@onclick='addToCart(12)']")


class Dell_i7(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=12")


    # Getters

    def get_dell_i7_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(dell_i7_name))
    def get_dell_i7_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(dell_i7_price))
    def get_button_dell_i7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_dell_i7))


    # Actions
    def click_dell_i7(self):
        self.get_button_dell_i7().click()