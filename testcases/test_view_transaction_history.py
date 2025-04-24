import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pageObjects.TransactionHistoryPage import TransactionHistoryPage
from utilities.custom_logger import custom_logger

logger = custom_logger()

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    logger.info("🚀 Launching ParaBank")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    yield driver
    logger.info("🛑 Closing browser")
    driver.quit()

def test_transaction_history(setup):
    driver = setup
    transaction_page = TransactionHistoryPage(driver)

    try:
        logger.info("🔐 Logging in with username 'john'")
        driver.find_element(By.NAME, "username").send_keys("john")
        driver.find_element(By.NAME, "password").send_keys("demo")
        driver.find_element(By.XPATH, "//input[@value='Log In']").click()

        logger.info("📊 Navigating to Accounts Overview")
        transaction_page.click_account_overview()

        logger.info("📂 Selecting account (e.g., 13122)")
        transaction_page.select_account()

        logger.info("📅 Selecting 'All' in month dropdown")
        transaction_page.select_month("All")

        logger.info("📑 Selecting 'All' in transaction type dropdown")
        transaction_page.select_transaction_type("All")

        logger.info("✅ Checking transaction table rows")
        transaction_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='transactionTable']//tr[position()>1]"))
        )
        assert len(transaction_rows) > 0, "❌ No transactions found in the table."
        logger.info(f"🧾 {len(transaction_rows)} transactions found")

        for index, row in enumerate(transaction_rows, start=1):
            columns = row.find_elements(By.TAG_NAME, "td")
            assert len(columns) >= 3, f"❌ Row {index} does not contain all required fields (Date, Description, Amount)."
            logger.info(f"✅ Row {index} contains Date, Description, Amount")

        logger.info("🎉 Transaction history test passed successfully")

    except TimeoutException as e:
        logger.error(f"❌ Test failed due to timeout: {e}")
        driver.save_screenshot("screenshots/transaction_history_failure.png")
        pytest.fail(f"Test failed due to timeout: {e}")
