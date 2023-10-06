from selenium.webdriver.common.by import By

from pageobjects.Shippingpage import Shipping


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    confirmButton = (By.CSS_SELECTOR, ".btn-success")

    def ConfirmButton(self):
        self.driver.find_element(*Confirm.confirmButton).click()
        return Shipping(self.driver)
