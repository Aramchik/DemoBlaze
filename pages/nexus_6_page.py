from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage


# Lockator
button_add_to_cart_nexus = (By.XPATH, "//a[@onclick='addToCart(3)']")
nexus_name = (By.XPATH, "//*[text()='Nexus 6']")
nexus_price = (By.XPATH, "//*[text()='$650']")



# Class for Nexus 6 page
class Nexus_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a Nexus 6 page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=3")


    # Getters

    def get_nexus_name(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(nexus_name))

    def get_nexus_price(self):
        return WebDriverWait(self.browser, 10).until(Ec.visibility_of_element_located(nexus_price))
    def get_button_nexus(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_nexus))



    # Actions
    def click_nexus(self):
        self.get_button_nexus().click()