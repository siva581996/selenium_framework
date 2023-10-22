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
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(3)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.current_window_handle)
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='wikipedia-search-results']")))

links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']")

for link in links:
    #driver.find_element(By.XPATH, "//div[@class='wikipedia-search-results']/child::div/a").click()
    link.find_element(By.XPATH, "a").click()


windowids = driver.window_handles
print(windowids)
n = 1
for i in windowids:
    print("window id of window {} :{} ".format(n, i))
    driver.switch_to.window(i)
    print(driver.title)
    n += 1

for j in windowids:
    driver.switch_to.window(j)

    if driver.title == "Selenium dioxide - Wikipedia" or driver.title == "Selenium disulfide - Wikipedia" or driver.title == "Selenium (software) - Wikipedia" or driver.title == "Selenium in biology - Wikipedia":
        driver.close()
