from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[EnvironmentError])


wait.until(EC.visibility_of_element_located((By.XPATH, "")))

