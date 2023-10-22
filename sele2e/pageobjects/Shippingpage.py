from selenium.webdriver.common.by import By


class Shipping:
    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    check = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    confirmmessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def countryname(self):
        return self.driver.find_element(*Shipping.countryName)

    def countrycnfrm(self):
        return self.driver.find_element(*Shipping.country)

    def checkbox(self):
        return self.driver.find_element(*Shipping.check)


    def confirm_message(self):
        return self.driver.find_element(*Shipping.confirmmessage)

    def purchase_button(self):
        return self.driver.find_element(*Shipping.purchase)
