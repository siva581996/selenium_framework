import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(3)
driver.maximize_window()
wait = WebDriverWait(driver, 20, poll_frequency=2)

driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.XPATH, "//a")
print("Total links present:", len(links))

broken = 0
valid = 0

for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)

    except:
        None

    if res.status_code >= 400:
        print("{} is a broken link".format(url))
        broken += 1

    else:
        print("{} is a valid link".format(url))
        valid += 1


print("Total broken link :", broken)
print("Total valid link :", valid)
