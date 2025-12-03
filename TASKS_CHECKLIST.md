# TASKS CHECKLIST

A task checklist will be provided in order to showcase the high-level test scenarios and verifications used to validate the "Create Task" feature works as expected.

## 1. The user logs in from the SimplePracite authentication page
- The user will open the SimplePractice login page
- The user will submit their valid credentials to login
- Validate the user has login correctly by confirming the URL has changed and waiting for the presence of dashboard elements (e.g. User Avatar)

## 2. The user navigates to the Tasks page
- The user will select the Tasks tab from the dashboard/calendar page

## 3. The user creates a new task
- The user will create a new task by selecting the Create New Task button
- A "Create Task" form will open 
- The user will enter a unique title for the Task
- The user will enter a description
- The user will set a due date by interacting with a calendar
- The user will set a time by interacting with the time picker (hour, minute, AM/PM)
- The user will select a Priority from a dropdwon menu (e.g. High)
- The user will look up for a Client by using a search box and will select the Client from a dropdown (e.g. John Doe)
- The user will select a Team Member from the dropdown menu (e.g. Test Automation)
- The user will attach one or more files to the Task form (e.g. [PatientInformationRecrod.pdf, requirements.txt])
- The user will save the new task

## 4. Verify the new task was created succesfully
- A new task will be created and listed
- The task creation will be validated by making sure the fields (title and status) are displayed as expected

## 5. The user will complete the task
- The user will filter their tasks by using the status filter "Incomplete"
- The user will complete the task by selecting the checkbox and marking the task as Completed

# 6. Verify the task completion
- The user will filter their tasks by using the status filter "Completed"
- All completed tasks will be displayed with a checkbox marked
- The task completion will be validated by inspecting the checkbox status.

