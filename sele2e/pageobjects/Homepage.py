from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.Shoppingpage import Shoppingpage


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "div[class='form-group'] input[name='name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    icecream = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    stat = (By.ID, "inlineRadio2")

    def shop_items(self):
        self.driver.find_element(*Homepage.shop).click()
        return Shoppingpage(self.driver)

    def insert_name(self):
        return self.driver.find_element(*Homepage.name)

    def insert_email(self):
        return self.driver.find_element(*Homepage.email)

    def insert_pwd(self):
        return self.driver.find_element(*Homepage.pwd)

    def ice(self):
        return self.driver.find_element(*Homepage.icecream)

    def gend(self):
        return(self.driver.find_element(*Homepage.gender))

    def pri(self):
        s ="message successful"
        return s
    def status(self):
        return self.driver.find_element(*Homepage.stat)

    def submit(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

    def texted(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text


