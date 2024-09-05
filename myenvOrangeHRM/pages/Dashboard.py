from Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By

class DashboardPage(SeleniumHelper):

    TXT_DASHBOARD = (By.XPATH, "//div[@id='content']/div/div[1]/h1")

    def __init__(self, driver):
        super().__init__(driver)

    def validatePageLoaded(self):
        self.verify_element_displayed(self.TXT_DASHBOARD)
        assert self.get_element_text(self.TXT_DASHBOARD) == "Dashboard"