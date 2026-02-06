import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base_page import BasePage


# Lockators
# sign_up
sign_up_button = (By.XPATH, "//a[@id='signin2']")

user_name = (By.XPATH, "//input[@id='sign-username']")
password = (By.XPATH, "//input[@id='sign-password']")

sign_up_button_window = (By.XPATH, "//div[@class='modal-footer']//button[contains(text(), 'Sign up')]")
close_button_window = (By.XPATH, "//*[@id='signInModal']//button[contains(text(), 'Close')]")


# Lockators
# log_in
log_in_button = (By.XPATH, "//a[@id='login2']")

user_name_li = (By.XPATH, "//input[@id='loginusername']")
password_li = (By.XPATH, "//input[@id='loginpassword']")

log_in_button_window = (By.XPATH, "//button[@onclick='logIn()']")
close_button_window_li = (By.XPATH, "//*[@id='logInModal']//button[contains(text(), 'Close')]")

welcome_admin = (By.XPATH,"//*[@id='nameofuser']")



# After Log in
# lockator
welcome = (By.XPATH,"//a[@id='nameofuser']")




# Class for Sign up page
class Sign_Up(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    # Open home page
    def open(self):
        self.browser.get("https://www.demoblaze.com/index.html")


    # Getters
    # Sign Up
    def get_sign_up_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(sign_up_button))

    def get_user_name(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(user_name))

    def get_password(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(password))

    def get_sign_up_button_window(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(sign_up_button_window))

    def get_close_button_window(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(close_button_window))






    # Getters log in

    def get_log_in_buuton(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(log_in_button))

    def get_user_name_li(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(user_name_li))

    def get_password_li(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(password_li))

    def get_log_in_button_window(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(log_in_button_window))

    def get_close_button_window_li(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(close_button_window_li))





    # Actions
    # Sign up
    def click_sign_up_button(self):
        self.get_sign_up_button().click()



    def click_sign_up_window(self):
        self.get_sign_up_button_window().click()


    def perform_sign_up(self, max_attempts=3):
        attempt = 0
        while attempt < max_attempts:
            try:
                # Получаем или генерируем новые данные для текущей попытки
                credentials = self.get_credentials()
                self.get_user_name().send_keys(credentials["username"])
                print(f'Attempt {attempt + 1}: Enter username {credentials["username"]}')
                self.get_password().send_keys(credentials["password"])
                print(f'Attempt {attempt + 1}: Enter password {credentials["password"]}')
                self.get_sign_up_button_window().click()
                print(f'Attempt {attempt + 1}: Click sign up')

                # Ожидание результата (успешного или alert)
                WebDriverWait(self.browser, 3).until(Ec.alert_is_present())
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                if "This user already exist" in alert_text:
                    print(f'Attempt {attempt + 1} failed: {alert_text}')
                    alert.accept()
                    # Генерируем новые данные для следующей попытки
                    self.credentials = {
                        "username": self.fake.user_name(),
                        "password": self.fake.password(),
                        "email": self.fake.email()
                    }
                    attempt += 1
                    continue
                else:
                    alert.accept()
                    print(f'Attempt {attempt + 1} succeeded with unexpected alert: {alert_text}')
                    break
            except Exception as e:
                print(f'Attempt {attempt + 1} error: {e}')
                attempt += 1
                if attempt < max_attempts:
                    # Очищаем поля и генерируем новые данные
                    self.get_user_name().clear()
                    self.get_password().clear()
                    self.credentials = {
                        "username": self.fake.user_name(),
                        "password": self.fake.password(),
                        "email": self.fake.email()
                    }
                    continue
                raise

        if attempt == max_attempts:
            raise Exception(f"Failed to sign up after {max_attempts} attempts")

        # Ожидание возвращения на главную страницу
        WebDriverWait(self.browser, 10).until(Ec.url_to_be("https://www.demoblaze.com/index.html"))
        print("Successfully signed up and redirected to home page")



    def close_window_su(self):
        self.get_close_button_window().click()




    # Actions
    # Log in

    def click_log_in(self):
        self.get_log_in_buuton().click()


    def click_log_in_window(self):
        self.get_log_in_button_window().click()



    def perform_login(self):
        credentials = self.get_credentials()
        self.get_user_name_li().send_keys(credentials["username"])
        print('Enter username')
        self.get_password_li().send_keys(credentials["password"])
        print('Enter password')
        self.get_log_in_button_window().click()
        print('Click log in')





    # Getter welcome
    def get_welcome(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(welcome))

        # Getter welcome

    def get_welcome_admin(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(welcome_admin))


    def assert_welcome(self):
        assert self.get_welcome_admin().text == 'Welcome admin'
        print('Log in successfull')