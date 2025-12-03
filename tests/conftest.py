from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


def pytest_addoption(parser):
    """Register a browser option (--browser) to select which browser webdriver will be used.

    Usage examples:
      - pytest --browser=edge
      - pytest --browser=chrome
      - pytest --browser=firefox
    Default: edge
    """
    parser.addoption("--browser", action="store", default="edge",
                     help="Browser to run tests: Firefox, Edge or Chrome (default: Edge)")


@pytest.fixture()
def driver(request):
    """Create and yield a webdriver instance based on the --browser option.
    - Edge/Chrome: window size set via --window-size=1920,1080
    - Firefox: window size set via --width/--height
    - Sets a 30s page load timeout
    - Ensures a teardown method to close the browser after the test session
    """
    browser=request.config.getoption("--browser", default="edge").lower()
    if browser == "edge":
        options = EdgeOptions()
        options.add_argument("--window-size=1920,1080")
        my_driver =  webdriver.Edge(options=options)     
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        my_driver =  webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        my_driver =  webdriver.Chrome(options=options)      
    else:
        raise TypeError(f"Expected 'edge', 'chrome' or 'firefox', but received {browser}")  

    my_driver.set_page_load_timeout(30)
    yield my_driver
    print("\nClosing web browser")
    my_driver.quit()

