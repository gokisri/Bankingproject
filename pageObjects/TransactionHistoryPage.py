from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransactionHistoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_overview_xpath = "//a[normalize-space()='Accounts Overview']"
        self.account_table_first_account_xpath = "//table[@id='accountTable']//tr[1]//td[1]//a"
        self.select_month_xpath = "//select[@id='month']"
        self.select_month_all_xpath = "//select[@id='month']//option[@value='All'][normalize-space()='All']"
        self.select_type_xpath = "//select[@id='transactionType']"
        self.select_type_all_xpath = "//select[@id='transactionType']//option[@value='All'][normalize-space()='All']"

    def click_account_overview(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.account_overview_xpath))
        ).click()

    def select_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.account_table_first_account_xpath))
        ).click()

    def select_month(self, month="All"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_month_xpath))
        ).click()
        if month == "All":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.select_month_all_xpath))
            ).click()

    def select_transaction_type(self, transaction_type="All"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_type_xpath))
        ).click()
        if transaction_type == "All":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.select_type_all_xpath))
            ).click()

    def verify_transaction_history_page(self):
        """Verifies that transaction table headers are visible (Date, Description, Amount)."""
        headers_xpath = "//table[@id='transactionTable']//th"
        headers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, headers_xpath))
        )
        header_texts = [header.text for header in headers]
        assert "Date" in header_texts, "❌ Date column not found in transaction table!"
        assert "Description" in header_texts, "❌ Description column not found!"
        assert "Amount" in header_texts, "❌ Amount column not found!"
