from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

countries = driver.find_element(By.ID, "country")
country = Select(countries)

#country.select_by_value("uk")
country.select_by_index(1)

allopp = country.options
print(len(allopp))

for opp in allopp:
    if opp.text == "Germany":
        opp.click()
        break



