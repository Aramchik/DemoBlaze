import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage

# Lokator Place Order button
place_order_button = (By.XPATH,"//button[@class='btn btn-success']")


# Lokators #Локаторы чек-аута
first_name = (By.XPATH, "//input[@id='name']")
country = (By.XPATH, "//input[@id='country']")
city = (By.XPATH, "//input[@id='city']")
credit_card = (By.XPATH, "//input[@id='card']")
month = (By.XPATH, "//input[@id='month']")
year = (By.XPATH, "//input[@id='year']")

purchase = (By.XPATH, "//button[@onclick='purchaseOrder()']")
close = (By.XPATH, "(//button[@class='btn btn-secondary'])[3]")

success_text = (By.XPATH,"//*[text()='Thank you for your purchase!']")
ok_button = (By.XPATH, "//button[@class='confirm btn btn-lg btn-primary']")



class Cart_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    # Open cart page
    def open(self):
        self.browser.get("https://www.demoblaze.com/cart.html")


    # Getter Place Order button
    def get_place_order_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(place_order_button))





    # Getter check-out

    def get_name(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(first_name))


    def get_country(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(country))

    def get_city(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(city))

    def get_credit_cart(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(credit_card))


    def get_month(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(month))

    def get_year(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(year))


    def get_close(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(close))


    def get_purchase(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(purchase))






    # getter success
    def get_success_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(success_text))

    def get_ok(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(ok_button))







    # Actions

    # Click Opder Place button
    def click_order_button(self):
        self.get_place_order_button().click()



    # Text check-out info

    def send_info(self):
        self.get_name().send_keys(self.name)
        print("Enter Name")
        time.sleep(1)

        self.get_country().send_keys(self.country)
        print("Enter Country")
        time.sleep(1)

        self.get_city().send_keys(self.city)
        print("Enter City")
        time.sleep(1)

        self.get_credit_cart().send_keys(self.credit_card)
        print("Enter Credit Card")
        time.sleep(1)

        self.get_month().send_keys(self.month)
        print("Enter Month")
        time.sleep(1)

        self.get_year().send_keys(self.year)
        print("Enter Year")
        time.sleep(1)




    # Click Purchae button
    def click_purchase(self):
        self.get_purchase().click()


    # Click ok
    def click_ok(self):
        self.get_ok().click()



    # Click close
    def click_close(self):
        self.get_close().click()