from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage


# Lockators
# CATEGORIES
phones = (By.XPATH, '''//a[@onclick="byCat('phone')"]''')
laptops = (By.XPATH,'''//a[@onclick="byCat('notebook')"]''')
monitors = (By.XPATH, '''//a[@onclick="byCat('monitor')"]''')


# cart
cart = (By.ID,"cartur")


# Phones
samsung_galaxy_s6 = (By.XPATH, "//*[text()='Samsung galaxy s6']")
nokia_lumia_1520 = (By.XPATH, "//*[text()='Nokia lumia 1520']")
nexus_6 = (By.XPATH, "//*[text()='Nexus 6']")
samsung_galaxy_s7 = (By.XPATH,"//*[text()='Samsung galaxy s7']")
iphone_6_32 = (By.XPATH,"//*[text()='Iphone 6 32gb']")
Sony_xperia_z5 = (By.XPATH,"//*[text()='Sony xperia z5']")
HTC_One_M9 = (By.XPATH,"//*[text()='HTC One M9']")


# Laptops
sony_vaio_i5 = (By.XPATH,"//*[text()='Sony vaio i5']")
sony_vaio_i7 = (By.XPATH,"//*[contains(text(), 'Sony vaio i7')]")
macbook_air = (By.XPATH,"//*[text()='MacBook air']")
dell_i7_8 = (By.XPATH,"//*[text()='Dell i7 8gb']")
dell_2017_15_inch = (By.XPATH, "//*[text()='2017 Dell 15.6 Inch']")
macbook_pro = (By.XPATH, "//*[text()='MacBook Pro']")



# Monitors
apple_monitor_24 = (By.XPATH, "//*[text()='Apple monitor 24']")
asus_full_hd = (By.XPATH, "//*[text()='ASUS Full HD']")



# Class for Main page
class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    # Open home page
    def open(self):
        self.browser.get("https://www.demoblaze.com/index.html")



    # getter cart
    def get_cart(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(cart))





    # Getter phones category
    def get_phones(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(phones))


    # Getter laptops category
    def get_laptops(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(laptops))


    # Getter monitors category
    def get_monitors(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(monitors))





    # Getters phones
    def get_sgs6(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(samsung_galaxy_s6))


    def get_nokia(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(nokia_lumia_1520))


    def get_nexus(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(nexus_6))


    def get_Samsung_galaxy_s7(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(samsung_galaxy_s7))


    def get_iphone6_32(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(iphone_6_32))


    def get_sony_xperia_z5(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(Sony_xperia_z5))


    def get_htc_one_m9(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(HTC_One_M9))





    # Getters laptops
    def get_sony_vaio_i5(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(sony_vaio_i5))


    def get_sony_vaio_i7(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(sony_vaio_i7))


    def get_macbook_air(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(macbook_air))


    def get_dell_i7(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(dell_i7_8))


    def get_dell_2017(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(dell_2017_15_inch))


    def get_macbook_pro(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(macbook_pro))




    # Getters monitors
    def get_apple_monitor_24(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(apple_monitor_24))


    def get_asus_full_hd(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(asus_full_hd))





    # Actions

    # Click phones category
    def click_phones(self):
        self.get_phones().click()



    # Clcik cart
    def click_cart(self):
        self.get_cart().click()



    # Click phones
    def click_sgs6(self):
        self.get_sgs6().click()


    def click_nokia(self):
        self.get_nokia().click()


    def click_nexus(self):
        self.get_nexus().click()


    def click_sgs7(self):
        self.get_Samsung_galaxy_s7().click()


    def click_iphone6_32(self):
        self.get_iphone6_32().click()


    def click_sony_xperia_z5(self):
        self.get_sony_xperia_z5().click()


    def click_htc_one_m9(self):
        self.get_htc_one_m9().click()





    # Click laptops category

    def click_laptops(self):
        self.get_laptops().click()




    # Click laptops
    def click_sony_vaio_i5(self):
        self.get_sony_vaio_i5().click()


    def click_sony_vaio_i7(self):
        self.get_sony_vaio_i7().click()


    def click_macbook_air(self):
        self.get_macbook_air().click()


    def click_dell_i7(self):
        self.get_dell_i7().click()


    def click_dell_2017(self):
        self.get_dell_2017().click()


    def click_macbook_pro(self):
        self.get_macbook_pro().click()




    # Click monitors category

    def click_monitor_category(self):
        self.get_monitors().click()





    # click monitors
    def click_apple_monitor_24(self):
        self.get_apple_monitor_24().click()


    def click_asus_full_hd(self):
        self.get_asus_full_hd().click()


