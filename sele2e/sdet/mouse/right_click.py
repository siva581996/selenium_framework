import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 20)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
act = ActionChains(driver)

button = driver.find_element(By.XPATH, "//span[normalize-space()='right click me']")
act.context_click(button).perform()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Quit']")))

driver.find_element(By.XPATH, "//span[normalize-space()='Quit']").click()
time.sleep(5)
pop = driver.switch_to.alert
print(pop.text)
pop.accept()

