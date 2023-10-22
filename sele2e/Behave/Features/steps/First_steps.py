from selenium import webdriver
from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('webdriver launched')
def launch_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service_obj = Service()
    context.driver = webdriver.Chrome(options=options, service=service_obj)
    context.driver.implicitly_wait(4)
    context.driver.maximize_window()


@when('website loaded successfully')
def launch_website(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify the logo present')
def step_impl(context):
    logo = context.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-logo").is_displayed()
    assert logo is True
#    print("logo displayed")


@then('Close browser')
def close_browser(context):
    context.driver.close()
