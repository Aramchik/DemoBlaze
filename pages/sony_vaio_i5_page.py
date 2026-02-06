from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
sony_vaio_i5_name = (By.XPATH, "//*[text()='Sony vaio i5']")
sony_vaio_i5_price = (By.XPATH,"//*[text()='$790']")

button_add_to_cart_sony_vaio_i5 = (By.XPATH, "//a[@onclick='addToCart(8)']")




class Sony_vaio_i5(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=8")


    # Getters
    def get_name_svi5(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_vaio_i5_name))
    def get_price_svi5(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sony_vaio_i5_price))
    def get_button_svi5(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_sony_vaio_i5))


    # Actions
    def click_svi5(self):
        self.get_button_svi5().click()