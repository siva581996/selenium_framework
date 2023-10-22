from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//div[@class='form-group'][4]/child::div")
print(len(checkboxes))
for checkbox in checkboxes:
    dayname = checkbox.text
    print(dayname)
    if dayname == 'Monday':
        checkbox.click()

