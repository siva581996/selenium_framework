import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Alert']").click()
time.sleep(10)
pop = driver.switch_to.alert
pop.accept()
