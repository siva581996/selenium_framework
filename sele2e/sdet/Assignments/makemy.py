import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 10)
driver.get("https://www.makemytrip.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".commonModal__close").click()
driver.find_element(By.XPATH, "//label[@for='fromCity']").send_keys("chennai")

from_cities = driver.find_elements(By.CSS_SELECTOR, "p.font14.appendBottom5.blackText")
print(len(from_cities))
for city in from_cities:
    if city.text == "Chennai, India":
        print(city.text)
        city.click()

        break

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@for='toCity']")))
driver.find_element(By.XPATH, "//label[@for='toCity']").send_keys("goa")

to_cities = driver.find_elements(By.CSS_SELECTOR, "p.font14.appendBottom5.blackText")
print(len(to_cities))
for tcity in to_cities:
    if tcity.text == "Goa - Dabolim Airport, India":
        print(tcity.text)
        tcity.click()

