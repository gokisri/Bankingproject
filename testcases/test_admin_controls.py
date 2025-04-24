import pytest
from pageObjects.AdminPage import AdminPage
from utilities.custom_logger import custom_logger
from utilities.read_properties import ReadConfig

class Test_Admin_Controls:
    baseURL = ReadConfig.getApplicationURL()
    logger = custom_logger()

    @pytest.mark.sanity
    def test_admin_page_controls(self, setup):
        self.driver = setup
        self.driver.get("https://parabank.parasoft.com/parabank/admin.htm")
        self.admin = AdminPage(self.driver)

        try:
            self.logger.info("===== Starting Admin Page Controls Test =====")

            self.logger.info("Navigating to Admin Page...")
            self.admin.goToAdminPage()  # Ensure this exists

            self.logger.info("Clicking Initialize button...")
            self.admin.clickInitialize()

            self.logger.info("Toggling SOAP service...")
            self.admin.toggleSOAPService()

            self.logger.info("Selecting REST XML mode...")
            self.admin.selectRESTXMLMode()

            self.logger.info("Selecting REST JSON mode...")
            self.admin.selectRESTJSONMode()

            self.logger.info("Clicking Submit button...")
            self.admin.clickSubmit()

            self.logger.info("✅ Admin Page Controls Test Passed")
            assert True

        except Exception as e:
            self.logger.error(f"❌ Test Failed: {str(e)}")
            self.driver.save_screenshot("screenshots/test_admin_page_controls.png")
            assert False
