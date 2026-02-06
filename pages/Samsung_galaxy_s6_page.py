from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage


# Lockator
samsung_s6_name = (By.XPATH, "//*[text()='Samsung galaxy s6']")
samsung_s6_price = (By.XPATH,"//*[text()='$360']")

button_add_to_cart_samsung_s6 = (By.XPATH, "//a[@onclick='addToCart(1)']")

# Class for Samsung galaxy s6 page
class Samsung_s6_Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=1")



    # Getters

    def get_samsung_name(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(samsung_s6_name))


    def get_samsung_price(self):
        return WebDriverWait(self.browser, 10).until(Ec.visibility_of_element_located(samsung_s6_price))



    def get_button_sgs6(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_samsung_s6))




    # Actions
    def click_sgs6(self):
        self.get_button_sgs6().click()