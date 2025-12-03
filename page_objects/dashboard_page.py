from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class DashboardPage(BasePage):
    """Dashboard Page Object: top-level actions and navigation from the main app dashboard."""
    
    url = "https://secure.simplepractice.com/calendar/appointments"

    #Locators
    avatar_icon = (By.ID, "user-avatar")
    messaging_button = (By.CSS_SELECTOR, ".MessagingClientToggleButton")
    create_button = (By.CSS_SELECTOR, ".button-link.button-navbar.create")
    announcement_button = (By.CSS_SELECTOR, ".button-link.button-navbar[aria-label='announcements']")
    search_box = (By.ID, "spds-input-search-container-6-trigger-input")
    promo_button = (By.CSS_SELECTOR, ".button-promo")
    create_client_button = (By.XPATH, "//button[contains(., 'Create client')]")

    
    def __init__(self, driver: WebDriver):
        """Store the WebDriver and initialize BasePage."""
        self.__init__(driver)

    def create_client(self):
        """Open the global 'Create' menu and navigate to the 'Create client' flow."""
        super().click(self.create_button)
        super().click(self.create_client_button)

