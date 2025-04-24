import pytest
from pageObjects.login_page import LoginPage
from pageObjects.open_account_page import OpenAccountPage
from utilities.custom_logger import custom_logger  # Assuming your logger function is named this
import os

@pytest.mark.regression
class Test_OpenNewAccount:
    logger = custom_logger()

    def test_open_new_account(self, setup):
        self.logger.info("********** TC_CUST_01_OpenNewAccount STARTED **********")
        self.driver = setup
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.logger.info("Navigated to ParaBank homepage")

        try:
            # Login Step
            login_page = LoginPage(self.driver)
            login_page.setUserName("john")
            login_page.setPassword("demo")
            login_page.clickLogin()
            self.logger.info("✅ Logged into customer account")

            # Open New Account Page
            open_account_page = OpenAccountPage(self.driver)
            open_account_page.navigate_to_open_new_account()
            self.logger.info("Navigated to 'Open New Account' page")

            open_account_page.select_account_type("SAVINGS")
            self.logger.info("Selected 'SAVINGS' account type")

            open_account_page.select_existing_account()
            self.logger.info("Selected existing account for funding")

            open_account_page.click_open_new_account()
            self.logger.info("Clicked on 'Open New Account' button")

            # Assertion Section
            new_account_number = open_account_page.get_new_account_number()
            success_message = open_account_page.get_success_message()

            assert new_account_number is not None and new_account_number != "", "❌ New account number not displayed!"
            assert success_message == "Congratulations, your account is now open.", f"❌ Unexpected success message: {success_message}"

            self.logger.info(f"✅ Account created with Account Number: {new_account_number}")
            self.logger.info("********** TC_CUST_01_OpenNewAccount COMPLETED SUCCESSFULLY **********")

        except Exception as e:
            os.makedirs("Screenshots", exist_ok=True)
            self.driver.save_screenshot(".\\Screenshots\\test_open_new_account_failure.png")
            self.logger.error(f"❌ Test failed: {str(e)}")
            assert False
