from selenium.webdriver.common.by import By

# You'll note only locator tuples exist on every page object. Interactions per page
# aren't required as they're deliberately made page agnostic - see tasks > main_tasks
class MainPage:
    def __init__(self):
        self.about_menu = (By.ID, "navbarDropdown")