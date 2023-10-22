from selenium.webdriver.common.by import By

from pageobjects.Confirmpage import Confirm


class Shoppingpage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, ".btn-primary")

    def getCardTitle(self):
        return self.driver.find_elements(*Shoppingpage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*Shoppingpage.cardFooter)

    def getCheckout(self):
        self.driver.find_element(*Shoppingpage.checkoutButton).click()
        return Confirm(self.driver)
