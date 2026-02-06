from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lockator
dell_2017_name = (By.XPATH, "//*[text()='2017 Dell 15.6 Inch']")
dell_2017_price = (By.XPATH, "//*[@id='tbodyid']/div[5]/div/div/h5")
button_add_to_cart_dell_2017 = (By.XPATH, "//a[@onclick='addToCart(13)']")


class Dell_2017(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Function to open a page
    def open(self):
        self.browser.get("https://www.demoblaze.com/prod.html?idp_=13")


    # Getters
    def get_dell_2017_name(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(dell_2017_name))
    def get_dell_2017_price(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(dell_2017_price))
    def get_button_dell_2017(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(button_add_to_cart_dell_2017))


    # Actions
    def click_dell_2017(self):
        self.get_button_dell_2017().click()