from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException

from webdriver_manager.chrome import ChromeDriverManager

from config import username, password, resident_map

from big_panda import properties, units


class double_rent_helper:
    ledger_xpath = "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody/tr[last()]/td[4]/a[4]"

    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.wait = WebDriverWait(self.driver, 10)
        self.primary_tab = None

    def login(self, username, password):
        try:
            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

    def reports_loop(self):
        for i in range(len(properties)):
            self.open_property(properties[i])
            self.open_unit(units[i])
            self.open_ledger()
            input("Press ENTER to continue...")
        self.driver.close()

    def open_property(self, property):
        change_property_link = self.driver.find_element(
            By.XPATH, "//a[contains(., 'CHANGE PROPERTY')]"
        )
        change_property_link.click()
        property_link = self.driver.find_element(
            By.XPATH, f"//a[contains(., '{property}')]"
        )
        property_link.click()

    def open_unit(self, unit):
        search_input = self.driver.find_element(By.NAME, "search_input")
        search_input.clear()
        search_input.send_keys(unit)
        search_input.send_keys(Keys.ENTER)

    def open_ledger(self):
        ledger_link = self.driver.find_element(By.XPATH, self.ledger_xpath)
        ledger_link.click()


if __name__ == "__main__":
    helper = double_rent_helper()
    helper.driver.get(resident_map)
    helper.login(username, password)
    helper.driver.maximize_window()
    helper.reports_loop()
