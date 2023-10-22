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
driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
developers = driver.find_element(By.ID, "developers-dd-toggle")
events = driver.find_element(By.XPATH, "//a[@title='Events']")

act = ActionChains(driver)

act.move_to_element(developers).perform()
act.move_to_element(events).click().perform()
