from base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver, testclass) -> None:
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.header_elem = self.driver.find_element_by_tag_name("h2")

        self.username_elem = self.driver.find_element_by_id("username")
        self.password_elem = self.driver.find_element_by_id("password")
        self.button_elem = self.driver.find_element_by_tag_name("button")

    def validate_page(self, is_valid: bool = True):
        if is_valid:
            self.testclass.assertIn("login", self.page_url)
            self.testclass.assertEqual("Login Page", self.header_elem.text)
            self.testclass.assertEqual("Login", self.button_elem.text)
        else:
            error_elem = self.driver.find_element_by_id("flash")
            self.testclass.assertIn("Your username is invalid!", error_elem.text)


    def perform_action(self, text1, text2):
        self.username_elem.send_keys(text1)
        self.password_elem.send_keys(text2)
        self.button_elem.click()
