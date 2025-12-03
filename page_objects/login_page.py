from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    """Login Page Object: handles navigation to login and the authentication flow."""
    #Locators
    url = 'https://account.simplepractice.com/'      
    username_field = (By.ID, "user_email")           
    password_field = (By.ID, "user_password")      
    submit_button =  (By.ID, "submitBtn")            
    forget_password = (By.CLASS_NAME, "forget-password-link")         
    error_message = (By.CSS_SELECTOR, ".alert.alert-error")            
    consent_banner = (By.CSS_SELECTOR, ".alert.cpt-ama-notice")          
    avatar_icon = (By.ID, "user-avatar")

    def __init__(self, driver: WebDriver):
        """Store the WebDriver and initialize BasePage."""
        super().__init__(driver)

    def open_login_page(self):
        """Navigate to the login page URL."""
        super().open_url(self.url)

    def start_login(self, username: str, password: str):
        """Perform login: fill credentials, submit, and wait for the avatar icon as a success cue."""
        super().type(self.username_field, username)
        super().type(self.password_field, password)
        super().click(self.submit_button)
        super().wait_until_element_is_visible(self.avatar_icon)

    def click_forgot_password(self):
        """Open the 'Forgot password' flow from the login page."""
        super().click(self.forget_password)
        
