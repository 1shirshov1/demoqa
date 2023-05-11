import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Crome()
    yield driver
    driver.quit()

    driver.set_window_size(width=1000, height=1000)