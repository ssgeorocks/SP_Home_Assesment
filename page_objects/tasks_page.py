from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage
import os 

class Tasks(BasePage):
    """Tasks Page Object: navigation, task creation, and assignment/attachments actions."""
    #Locators
    tasks_tab = (By.CSS_SELECTOR, 'a[href="/tasks"]')
    tasks_header = (By.XPATH, '//h1[text()="Tasks"]')
    create_task_button = (By.XPATH, '//a[@href="/tasks/new"]')
    task_name_field = (By.XPATH,'//input[@id="title"]')
    description_field = (By.XPATH,'//textarea[@id="description"]')
    due_on_calendar = (By.XPATH, '//input[@name="datePicker"]')
    next_calendar_button = (By.XPATH, "//th[@class='next']")
    time_picker_input = (By.XPATH, "//input[@id='timePicker']")
    time_picker_dropdown = (By.XPATH, "//div[contains(@class,'spds-input-time-picker-select')]")
    priority_container = (By.XPATH, "//label[@for='priority']")
    client_container = (By.XPATH, "//label[@for='client']")
    assigned_to_container = (By.XPATH, "//label[@for='taskAssignments']")
    save_task_button = (By.XPATH, "//button[contains(text(),'Save')]")
    cancel_task_button = (By.XPATH, "//button[contains(text(),'Cancel')]")
    file_input = (By.XPATH, "//input[@type='file']")
    order_tasks_button = (By.XPATH, "//button[@value='Custom']")

    def __init__(self, driver: WebDriver):
        """Initialize Tasks POM with a WebDriver."""
        super().__init__(driver)

    def open_tasks(self):
        """Open the Tasks page via top navigation."""
        super().click(self.tasks_tab)

    def is_task_page_loaded(self):
        """Return the page header text to confirm the Tasks page loaded."""
        header = super().get_text(self.tasks_header)
        return header
    
    def click_create_task(self):
        """Open the 'Create New Task' flow."""
        super().click(self.create_task_button)

    def fill_task_name(self, task_name: str):
        """Type the task title."""
        super().type(self.task_name_field, task_name)

    def fill_task_description(self, task_description: str):
        """Type the task description. Supports multiline text."""
        super().type(self.description_field, task_description)

    def select_date_from_calendar(self):
        """Pick a due date from the calendar widget (adjust day selection as needed)."""
        day = (By.XPATH, '//td[@class="day" and text()="7"]')
        super().click(self.due_on_calendar)
        super().click(self.next_calendar_button)
        super().click(day)

    def select_time_from_dropdown(self):
        """Select time components (hour/minute/period) in the time picker and confirm."""
        hour = (By.XPATH, "//li[@data-option-index='0.9']")
        minute = (By.XPATH, "//li[@data-option-index='1.2']")
        period = (By.XPATH, "//li[@data-option-index='2.0']")
        done_button =(By.XPATH, "//div[contains(@class, 'done-box-module')]//button[normalize-space(text()='Done')]")
        super().click(self.time_picker_dropdown)
        super().scroll_to(hour)
        super().click(hour)
        super().click(minute)
        super().click(period)
        super().click(done_button)

    def select_priority_from_dropdown(self, priority: str):
        """Select priority by visible text from the dropdown inside the priority container."""
        priority_dropdown = (By.XPATH, "//div[contains(@class,'spds-input-dropdown')]")
        priority_option = (By.XPATH, f"//button[@role='option' and text()='{priority}']")
        super().find_nested([self.priority_container, priority_dropdown]).click()
        super().click(priority_option)

    def select_client_from_dropdown(self, client: str):
        """Select a client by searching and choosing the matching option."""
        client_dropdown = (By.XPATH, "//div[contains(@class, 'select-box')]")
        client_searchbox = (By.CSS_SELECTOR, 'input.select-box__input')
        client_option = (By.XPATH, f"//div[@role='option' and text()='{client}']")
        element = super().find_nested([self.client_container, client_dropdown])
        element.click()
        super().type(client_searchbox, client)
        super().click(client_option)

    def select_team_member_from_dropdown(self, member: str):
        """Select the assignee (team member) from dropdown options."""
        assigned_dropdown = (By.XPATH, "//div[contains(@class, 'select-box')]")
        assigned_option = (By.XPATH, f"//div[@role='option']//span[text()='{member}']")
        super().click(assigned_dropdown)
        super().click(assigned_option)

    def attach_file_to_task(self, files: list[str]):
        """Attach one or more files to the task via the file input."""
        file_input = super().find(self.file_input)
        for f in files:
            path = os.path.abspath(f)
            file_input.send_keys(path)

    def save_task(self):
        """Click the Save button to persist the task."""
        super().click(self.save_task_button)

    def cancel_task(self):
        """Click the Cancel button to abort task creation/edit."""
        super().click(self.cancel_task_button)

    def is_task_created(self, title: str):
        """Return True if a task with the given title is present in the task list; False otherwise."""
        task = (By.XPATH, f"//button[contains(.,'{title}')]")
        try:
            super().find(task)
            return True
        except:
            return False


    def filter_task_by_status(self, status: str):
        """Open the status filter and select the given status (e.g., 'Incomplete', 'Completed')."""
        status_button = (By.XPATH, "//button[@type='button' and @value='Incomplete']")
        status_option = (By.XPATH, f"//button[@type='button' and contains(., '{status}')]")
        super().click(status_button)
        super().click(status_option)

    def order_tasks_by(self, driver, order_by: str):
        """Open the sort dropdown and order tasks by the provided label (e.g., 'Priority', 'Completed date')."""
        order_by_option = (By.XPATH, f"//button[@type='button' and contains(., '{order_by}')]")
        super().click(self.order_tasks_button)
        super().click(order_by_option)
        self.order_tasks_button = (By.XPATH, f"//button[@value='{order_by}']")

    def complete_task(self, title: str):
        """Mark the task with the given title as completed by clicking its checkbox/label."""
        task = (By.XPATH, f"//button[contains(.,'{title}')]/preceding::label[contains(@for,'isCompleted')][1]")
        super().click(task)

    def is_task_completed(self, title: str):
        """Return True if the task’s completion checkbox (preceding the title) is selected; False otherwise."""
        task = (By.XPATH, f"//button[contains(.,'{title}')]/preceding::input[@type='checkbox'][1]")
        state = super().find(task).is_selected()
        return state


