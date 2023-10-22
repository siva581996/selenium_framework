from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left = driver.find_element(By.XPATH, "//body").text
print(left)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
middle = driver.find_element(By.XPATH, "//body").text
print(middle)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
right = driver.find_element(By.XPATH, "//body").text
print(right)


