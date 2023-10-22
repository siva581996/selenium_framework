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
slide = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")

print("location ooooof slider before sliding: ", slide.location)

act.drag_and_drop_by_offset(slide, 159, 0).perform()

print("Location of slide after sliding: ", slide.location)
