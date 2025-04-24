import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.TransferFundsPage import TransferFundsPage
from utilities.custom_logger import custom_logger

logger = custom_logger()

@pytest.fixture
def setup():
    """Set up and tear down for the test."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    logger.info("🚀 Launching ParaBank application")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    yield driver
    logger.info("🛑 Closing browser")
    driver.quit()

def test_transfer_funds(setup):
    driver = setup
    try:
        logger.info("🔐 Logging in as 'john'")
        driver.find_element(By.NAME, "username").send_keys("john")
        driver.find_element(By.NAME, "password").send_keys("demo")
        driver.find_element(By.XPATH, "//input[@value='Log In']").click()

        transfer_funds_page = TransferFundsPage(driver)

        logger.info("💼 Navigating to Transfer Funds page")
        transfer_funds_page.click_transfer_funds_link()

        logger.info("💸 Entering amount to transfer: 500")
        transfer_funds_page.enter_amount("500")

        logger.info("🏦 Selecting 'From Account'")
        transfer_funds_page.select_from_account()

        logger.info("🏦 Selecting 'To Account'")
        transfer_funds_page.select_to_account()

        logger.info("📤 Clicking Transfer button")
        transfer_funds_page.click_transfer()

        logger.info("✅ Verifying success message")
        success_msg = transfer_funds_page.get_success_message()
        expected_msg = "Transfer Complete!"
        assert expected_msg in success_msg, f"Expected message: '{expected_msg}', but got: '{success_msg}'"
        logger.info("🎉 Transfer funds test passed successfully.")

    except Exception as e:
        logger.error(f"❌ Test failed due to exception: {e}")
        driver.save_screenshot("screenshots/transfer_funds_failure.png")
        raise
