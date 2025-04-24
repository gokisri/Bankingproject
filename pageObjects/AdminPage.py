from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    admin_page_xpath = "//a[normalize-space()='Admin Page']"
    link_initialize_xpath = "//button[normalize-space()='Initialize']"
    checkbox_soap_xpath = "//input[@id='accessMode1']"
    checkbox_restxml_xpath = "//input[@id='accessMode2']"  # used for both XML/JSON
    checkbox_restjson_xpath = "//input[@id='accessMode3']"
    checkbox_jdbc_xpath = "//input[@id='accessMode4']"
    button_submit_xpath = "//input[@value='Submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goToAdminPage(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.admin_page_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_page_xpath))).click()

    def clickInitialize(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_initialize_xpath))).click()

    def toggleSOAPService(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_soap_xpath))).click()

    def selectRESTXMLMode(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_restxml_xpath))).click()

    def selectRESTJSONMode(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_restjson_xpath))).click()

    def selectJDBCMode(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_jdbc_xpath))).click()

    def clickSubmit(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_submit_xpath))).click()
