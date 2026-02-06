from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
sony_vaio_i7_name = (By.XPATH, "//*[contains(text(),'Sony vaio i7')]")
sony_vaio_i7_price = (By.XPATH,"//*[text()='$790']")
button_add_to_cart_sony_vaio_i7 = (By.XPATH, "//a[@onclick='addToCart(9)']")


class Sony_vaio_i7(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=9")


    # Getters
    def get_name_svi7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_vaio_i7_name))
    def get_price_svi7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_vaio_i7_price))


    def get_button_svi7(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_sony_vaio_i7))


    # Actions
    def click_svi7(self):
        self.get_button_svi7().click()