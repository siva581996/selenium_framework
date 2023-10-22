import time

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

#BY pixel
# driver.execute_script("window.scrollBy(0, 800)","")
# value = driver.execute_script("return window.pageYOffset;")
# print(value)


#By Element
# slide = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
#
# driver.execute_script("arguments[0].scrollIntoView();", slide)
# value = driver.execute_script("return window.pageYOffset")
# print(value)

#Till end of the page

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window,scrollBy(0, -document.body.scrollHeight)")

