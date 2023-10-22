from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)
driver.maximize_window()
driver.get("https://www.facebook.com")
email = driver.find_element(By.ID, "email")
email.send_keys("email.com")
pwd = driver.find_element(By.CSS_SELECTOR, "input.inputtext[name='pass']")
pwd.send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()

driver.close()