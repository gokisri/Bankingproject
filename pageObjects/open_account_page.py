from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenAccountPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    link_open_new_account = (By.XPATH, "//a[normalize-space()='Open New Account']")
    dropdown_account_type = (By.XPATH, "//select[@id='type']")
    dropdown_existing_account = (By.XPATH, "//select[@id='fromAccountId']")
    btn_open_new_account = (By.XPATH, "//input[@value='Open New Account']")
    txt_success_message = (By.XPATH, "//p[normalize-space()='Congratulations, your account is now open.']")
    txt_new_account_number = (By.XPATH, "//a[@id='newAccountId']")

    # Actions
    def navigate_to_open_new_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.link_open_new_account)
        ).click()

    def select_account_type(self, account_type="SAVINGS"):
        dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dropdown_account_type)
        ))
        dropdown.select_by_visible_text(account_type)

    def select_existing_account(self):
        dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dropdown_existing_account)
        ))
        options = dropdown.options
        if options:
            dropdown.select_by_index(0)

    def click_open_new_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_open_new_account)
        ).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_success_message)
        ).text

    def get_new_account_number(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_new_account_number)
        ).text
