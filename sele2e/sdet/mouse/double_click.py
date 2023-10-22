from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 20)
driver.get("https://testautomationpractice.blogspot.com/")
act = ActionChains(driver)

val = driver.find_element(By.XPATH, "//input[@id='field1']")
val.clear()
val.send_keys("monkey D. Luffy")
butt = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(butt).perform()