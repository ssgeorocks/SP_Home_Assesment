# SimplePractice Home Assessment

This repository contains:
- Technical part: Selenium + Pytest POM framework automating the Tasks happy path.
- Analytical part: a Tasks happy-path checklist in `TASKS_CHECKLIST.md`.


## Requirements

- Python 3.10+
- A desktop browser installed: Edge (default), Chrome, or Firefox
- Optional: VS Code with Python extension

## Setup

1) Create and activate a virtual environment:
```sh
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows CMD
.\.venv\Scripts\activate.bat
```

2) Install dependencies:
```sh
pip install -r requirements.txt
```

Dependencies:
- pytest=8.4.2, selenium=4.38.0, pytest-html=4.1.1

Now you are ready to interact with the Pytest framework!

## Configuration

- Credentials are read from `data/test_data.py`
- You can select a browser by using the flag '--browser' from the command line:
  - `--browser=edge` (default), `--browser=chrome`, or `--browser=firefox`
- Test discovery and HTML report configured in `pytest.ini`.


### Environment variables (.env)
It is important to create or edit `.env.example` with valid credentials and then copy/rename it to `.env`:
- Set `SP_EMAIL` and `SP_PASSWORD` with the test account (provided with the assesment)
- Note: `.env` is git-ignored and should not be committed 


## Project Structure

- Page Objects:
  - Base: `page_objects/base_page.py`
  - Login: `page_objects/login_page.py`
  - Dashboard: `page_objects/dashboard_page.py`
  - Tasks: `page_objects/tasks_page.py`
- Tests:
  - Create task test (Home assesment): `tests/test_task.py`
- Config:
  - Pytest options: `pytest.ini`
  - Browser fixture: `tests/conftest.py`
- Data:
  - Credentials: `data/test_data.py`

## Running Tests

Run all tests (Edge by default):
```sh
pytest
```
Run the home assesment with edge browser:
```sh
pytest tests/test_task.py::test_create_task --browser=edge
```
Run the home assement test with chrome browser:
```sh
pytest tests/test_task.py::test_create_task --browser=chrome
```
Run the test with firefox browser:
```sh
pytest tests/test_task.py::test_create_task --browser=firefox
```

Run the home assesment test by marker (tasks):
```sh
pytest -m tasks --browser=firefox
```

Generate HTML report (also set in pytest.ini):
```sh
pytest --html=reports/report.html --self-contained-html
```

## VS Code

- Tests are discoverable via the Python Test Explorer.
- Edge is used by default if `--browser` is not specified.

## Troubleshooting

- “Cannot find Chrome binary”: Install Chrome or run with `--browser=edge`/`--browser=firefox`.
- Pytest cannot find tests: use explicit path or node
  - `pytest tests/test_task.py::test_create_task`


## Notes on Documentation
Parts of this documentation and some docstrings were assisted by AI. All content was reviewed, verified, and adapted by the author to reflect the actual codebase and test flow.

