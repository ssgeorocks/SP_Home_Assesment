from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
import time as Time

class BasePage:
    """Base POM con utilidades de espera, localización y acciones comunes sobre la UI."""
    def __init__(self, driver: WebDriver):
        """Store the WebDriver instance"""
        self.driver = driver

    def open_url(self, url: str):
        """Navigate to a given URL"""
        self.driver.get(url)

    def current_url(self):
        """Return the current URL"""
        return self.driver.current_url

    def wait_until_element_is_visible(self, locator: tuple, time: int = 10): 
        """Wait until the element located is visible."""
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def wait_until_element_is_clickable(self, locator: tuple, time: int = 10): 
        """Wait until the element located  is visible and clickcable"""
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.element_to_be_clickable(locator))
    
    def wait_until_element_is_present(self, locator: tuple, time: int = 10):
        """Wait until the element located is present in the DOM"""
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.presence_of_element_located(locator))
    
    def find(self, locator: tuple, time: int=10):
        """Find and return a WebElement"""
        self.wait_until_element_is_present(locator, time)
        return self.driver.find_element(*locator)
    
    def find_nested(self, locators: tuple, time: int=10):
        """Find a nested element by using sequence of locators"""
        self.wait_until_element_is_visible(locators[0], time)
        element = self.find(locators[0])
        for child in locators[1:]:
            element = element.find_element(*child)
        Time.sleep(3)
        return element
    
    def type(self, locator: tuple, text: str, time: int=10):
        """Type the given text into the element after waiting for visibility."""
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).send_keys(text)

    def click(self, locator: tuple, time: int=10):
        """Click the element located after waiting for clickability with a retry"""
        #self.wait_until_element_is_visible(locator, time)
        self.wait_until_element_is_clickable(locator, time)
        try:
            self.find(locator).click()
        except ElementClickInterceptedException:
            Time.sleep(5)
            self.find(locator).click()
        

    def get_text(self, locator: tuple, time: int = 10):
        """Return visible text of the element"""
        self.wait_until_element_is_visible(locator, time)
        return self.find(locator).text
    
    def scroll_to(self, locator:tuple, time: int = 10):
        """Scroll the page until the element"""
        self.wait_until_element_is_visible(locator, time)
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

