import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-0']").send_keys("sivakumar")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='RESULT_RadioButton-1_0']").click()
