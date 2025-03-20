import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.about_dropdown_menu import AboutDropdownMenu
from tasks.main_tasks import MainTasks

# Simple pytest tests at this stage. As you can see, we don't require any
# test-level pattern/design yet. But I intend to use Robot Framework here.
# As we add more tests, it will become apparent that we need this.

driver = webdriver.Chrome()
task = MainTasks(driver)

main_page = MainPage()
about_dropdown_menu = AboutDropdownMenu()
about_page = AboutPage()

@pytest.fixture
def setup_teardown():
    driver.get("https://selenium.dev")
    yield
    driver.quit()

def test_about_page_renders(setup_teardown):
    task.click_action(main_page.about_menu)
    task.click_action(about_dropdown_menu.about_selenium)
    result = task.assert_text_exists(about_page.about_selenium, "About Selenium")
    assert result