from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def next():
    driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


def prev():
    driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()


def day_m():
    dy = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    print(len(dy))
    for i in dy:
        print("Entered for loop")
        print(i.text)
        if i.text == day:
            print("i == 5")
            i.click()
            break


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
g_month = 'December'
year = '2023'
day = '20'
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

while True:

    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if yr == year:
        print("year is same")
        while True:
            d_mnth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            if months[d_mnth] == months[g_month]:
                print("month is also same")
                day_m()

                break

            elif months[d_mnth] > months[g_month]:
                print("month previous clicked")
                prev()

            elif months[d_mnth] < months[g_month]:
                print("month next clicked")
                next()


        break
    elif year < yr:
        print("previous clicked")
        prev()
    elif year > yr:
        print("next clicked")
        next()

