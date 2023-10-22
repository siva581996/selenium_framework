import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()

driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
#driver.get("https://testautomationpractice.blogspot.com/")
#popup Alert
# driver.find_element(By.XPATH, "//button[text()='Alert']").click()
# pop = driver.switch_to.alert
# print(pop.text)
# time.sleep(3)
# pop.accept()

# pop Dismiss
# driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
# pop = driver.switch_to.alert
# #pop.accept()
# pop.dismiss()
# print(driver.find_element(By.ID, "demo").text)


#pop Send value
# driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
# pop = driver.switch_to.alert
# pop.send_keys("Monkey D. Luffy")
# pop.accept()
# print(driver.find_element(By.ID, "demo").text)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
print(driver.find_element(By.TAG_NAME, "p").text)
driver.close()
