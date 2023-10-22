from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://www.facebook.com")
driver.maximize_window()

print(driver.find_element(By.XPATH, "//input[@name='email']").get_attribute('placeholder'))

logge = driver.find_element(By.XPATH, "//button[@name='login']")
print(logge.text)
print(logge.get_attribute('value'))