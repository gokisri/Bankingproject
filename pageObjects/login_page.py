from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@value='Log In']"
    button_logout_xpath = "//a[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setUserName(self, username):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath))).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_password_xpath))).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

    def clickLogout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))).click()
