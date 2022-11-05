import pytest
from selenium import webdriver
from Library.configuration import Configuration

@pytest.fixture(params=["Chrome"])
def init_driver(request): #request is a library
    global driver
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)
        driver.get(Configuration.URL)
        driver.maximize_window()
        yield driver
        # driver.close()