from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

countries = driver.find_element(By.CSS_SELECTOR, "#country")
country_name = Select(countries)

#country_name.select_by_visible_text("India")
#country_name.select_by_value('uk')
#country_name.select_by_index(3)

alloptions = country_name.options
print(len(alloptions))

for i in alloptions:
    if i.text == 'India':
        i.click()
        break

