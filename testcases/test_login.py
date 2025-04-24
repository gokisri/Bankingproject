import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import custom_logger  # Rename this for clarity
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = custom_logger()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_login(self, setup):
        self.logger.info("********** Starting test_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.logger.info("Entered Username")

        self.lp.setPassword(self.password)
        self.logger.info("Entered Password")

        self.lp.clickLogin()
        self.logger.info("Clicked Login Button")

        try:
            assert "ParaBank" in self.driver.title
            self.logger.info("✅ Login Test Passed")

            # Optional logout step
            self.lp.clickLogout()
            self.logger.info("Logged out successfully")

        except AssertionError:
            os.makedirs("Screenshots", exist_ok=True)
            self.driver.save_screenshot(".\\Screenshots\\test_login_failure.png")
            self.logger.error("❌ Login Test Failed - ParaBank title not found!")
            assert False
