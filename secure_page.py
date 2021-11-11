from base_page import BasePage


class SecurePage(BasePage):
    """ The secure login page"""

    def __init__(self, driver, testclass) -> None:
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.banner_elem = self.driver.find_element_by_id("flash")
        self.content_header = self.driver.find_element_by_css_selector(
            "#content h2")
        self.content_subheading = self.driver.find_element_by_css_selector(
            "h4.subheader")
        self.logout_elem = self.driver.find_element_by_css_selector("a.button")

    def validate_page(self):
        self.testclass.assertIn("secure", self.page_url)

        content_header_text = "Secure Area"
        self.testclass.assertIn(content_header_text, self.content_header.text)

        content_message = "Welcome to the Secure Area. When you are done click logout below."
        self.testclass.assertIn(content_message, self.content_subheading.text)

        self.testclass.assertIn("Logout", self.logout_elem.text)

        banner_text = "You logged into a secure area!"
        self.testclass.assertIn(banner_text, self.banner_elem.text)

    def perform_action(self):
        """ Log out of the page"""
        self.logout_elem.click()
