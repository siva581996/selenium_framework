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
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

oslo = driver.find_element(By.XPATH, "//div[@id='box1']")
stock = driver.find_element(By.XPATH, "//div[@id='box2']")
was = driver.find_element(By.XPATH, "//div[@id='box3']")
copen = driver.find_element(By.XPATH, "//div[@id='box4']")
seoul = driver.find_element(By.XPATH, "//div[@id='box5']")
rome = driver.find_element(By.XPATH, "//div[@id='box6']")
madrid = driver.find_element(By.XPATH, "//div[@id='box7']")

norway = driver.find_element(By.XPATH, "//div[@id='box101']")
sweden = driver.find_element(By.XPATH, "//div[@id='box102']")
us = driver.find_element(By.XPATH, "//div[@id='box103']")
den = driver.find_element(By.XPATH, "//div[@id='box104']")
korea = driver.find_element(By.XPATH, "//div[@id='box105']")
italy = driver.find_element(By.XPATH, "//div[@id='box106']")
spain = driver.find_element(By.XPATH, "//div[@id='box107']")

act = ActionChains(driver)

# act.drag_and_drop(oslo, norway).perform()
# act.drag_and_drop(stock, sweden).perform()
# act.drag_and_drop(was, us).perform()
# act.drag_and_drop(copen, den).perform()
# act.drag_and_drop(seoul, korea).perform()
# act.drag_and_drop(rome, italy).perform()
# act.drag_and_drop(madrid, spain).perform()

act.drag_and_drop(oslo, norway).drag_and_drop(stock, sweden).drag_and_drop(was, us).drag_and_drop(copen, den).drag_and_drop(seoul, korea).drag_and_drop(rome, italy).drag_and_drop(madrid, spain).perform()
