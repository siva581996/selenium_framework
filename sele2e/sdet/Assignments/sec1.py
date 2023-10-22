import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
email = driver.find_element(By.XPATH, "//input[@id='Email']")
pwd = driver.find_element(By.XPATH, "//input[@value='admin']")
email.clear()
pwd.clear()
time.sleep(5)
email.send_keys("admin@yourstore.com")
pwd.send_keys("admin")

driver.find_element(By.XPATH, "//input[@id='RememberMe']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Logout").click()

driver.close()
