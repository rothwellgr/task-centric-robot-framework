from selenium.webdriver.support.ui import WebDriverWait

class MainTasks:
    def __init__(self, driver):
        self.driver = driver

    # You'll note in the tests, that they're primarily driven by Tasks. They're interactions
    # with the page, decoupled from traidtional page objects. You pass page elements (well...
    # locator tuples) through them, where waits are applied to them in a page agnostic way.
    # You can separate and combine tasks, and split classes, as required.
    def click_action(self, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(lambda _ : self.driver.find_element(*locator))
        element.click()

    def assert_text_exists(self, locator, text):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(lambda _ : self.driver.find_element(*locator).text == text)