from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:
    def __init__(self, driver):
        self.driver = driver

    # XPaths
    transfer_fund_xpath = (By.XPATH, "(//a[normalize-space()='Transfer Funds'])[1]")
    amount_fund_xpath = (By.XPATH, "//input[@id='amount']")
    from_account_dropdown_xpath = (By.XPATH, "//select[@id='fromAccountId']")
    from_account_option_xpath = (
    By.XPATH, "//select[@id='fromAccountId']//option[@value='12456'][normalize-space()='12456']")
    to_account_dropdown_xpath = (By.XPATH, "//select[@id='toAccountId']")
    to_account_option_xpath = (
    By.XPATH, "//select[@id='toAccountId']//option[@value='12678'][normalize-space()='12678']")
    transfer_button_xpath = (By.XPATH, "//input[@value='Transfer']")

    # New Success Message XPath
    success_message_xpath = (By.XPATH, "//h1[normalize-space()='Transfer Complete!']")

    def click_transfer_funds_link(self):
        """Click the 'Transfer Funds' link."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.transfer_fund_xpath)).click()

    def enter_amount(self, amount):
        """Enter the amount for transfer."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.amount_fund_xpath)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.amount_fund_xpath)).send_keys(amount)

    def select_from_account(self):
        """Select the 'From Account' from dropdown."""
        from_account_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.from_account_dropdown_xpath))
        from_account_dropdown.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.from_account_option_xpath)).click()

    def select_to_account(self):
        """Select the 'To Account' from dropdown."""
        to_account_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.to_account_dropdown_xpath))
        to_account_dropdown.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_account_option_xpath)).click()

    def click_transfer(self):
        """Click the 'Transfer' button."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.transfer_button_xpath)).click()

    def get_success_message(self):
        """Get the success message after transferring funds."""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message_xpath)).text
