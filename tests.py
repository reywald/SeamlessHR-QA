import unittest
from selenium import webdriver
import time

# Import Page Objects
from home_page import HomePage
from login_page import LoginPage
from secure_page import SecurePage


class The_InternetTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.close()

    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")

        home_page = HomePage(driver, self)
        home_page.validate_page()
        home_page.perform_action()

        login_page = LoginPage(driver, self)
        login_page.validate_page(is_valid=True)
        login_page.perform_action("tomsmith" ,"SuperSecretPassword!")

        secure_page = SecurePage(driver, self)
        secure_page.validate_page()
        secure_page.perform_action()
        time.sleep(5)


    def test_invalid_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")

        home_page = HomePage(driver, self)
        home_page.validate_page()
        home_page.perform_action()

        login_page = LoginPage(driver, self)
        login_page.validate_page(is_valid=True)
        login_page.perform_action("thomas" ,"SuperSecretPassword!")
        login_page.validate_page(is_valid=False)
        time.sleep(5)
