from base_page import BasePage

class HomePage(BasePage):
    """ The home page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)
        
        self.page_url = self.driver.current_url
        self.page_title = "The Internet"
        self.link_elem = self.driver.find_element_by_link_text(
            "Form Authentication")

    def validate_page(self):
        self.testclass.assertEqual("https://the-internet.herokuapp.com/", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)
        

    def perform_action(self):
        self.link_elem.click()
