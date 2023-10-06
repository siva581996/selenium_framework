import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setups(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service_obj = Service()
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
