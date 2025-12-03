import pytest
from datetime import datetime
from page_objects.login_page import LoginPage
from page_objects.tasks_page import Tasks
from data.test_data import TEST_CREDENTIALS

@pytest.mark.tasks
def test_create_task(driver):
    """Test automation script that covers the following scenarios:
    1)Login
    2)Open Tasks and create a task with unique name
    3)Verify the task was created
    4)Complete the task
    5)Verify the task is marked as completed
    """
   #-------------------Test data -------------------
    timestamp = datetime.now().strftime("%d-%m-%y %H:%M")
    task_name = f"New task. [TEST {timestamp}]"
    task_description = "This a sample description for a test.\nThe description will be here."
    task_priority = "High"
    task_client = "John Doe"
    team_member = "Test Automation"
    attached_files = ["PatientInformationRecord.pdf", "attachment.txt"]

    #-------------------Login-------------------------
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.start_login(
        TEST_CREDENTIALS['email'],
        TEST_CREDENTIALS['password']
    )
    
    #-------------------Create task-------------------
    task_page = Tasks(driver)
    task_page.open_tasks()
    task_page.click_create_task()
    task_page.fill_task_name(task_name) 
    task_page.fill_task_description(task_description)
    task_page.select_date_from_calendar()
    task_page.select_time_from_dropdown()
    task_page.select_priority_from_dropdown(task_priority)
    task_page.select_client_from_dropdown(task_client)   
    task_page.select_team_member_from_dropdown(team_member)
    task_page.attach_file_to_task(attached_files)    
    task_page.save_task()
    assert task_page.is_task_created(task_name), f"Task {task_name} was not created correctly."

    #-------------------Complete task-------------------
    task_page.filter_task_by_status("Incomplete")
    #task_page.order_tasks_by(driver, "Priority")
    #task_page.complete_task('[TEST] This is a new task')
    task_page.complete_task(task_name)
    task_page.filter_task_by_status('Completed')
    #task_page.order_tasks_by(driver, "Completed date")
    task_status = task_page.is_task_completed(task_name)
    assert task_status == True, f'Task {task_name} was not completed.'
    