from pageobjects.Homepage import Homepage
from utilities.Basecls import Basecls


class Testone(Basecls):

    def test_e2e(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        shoppingpage = homepage.shop_items()
        log.info("getting all card details")
        products = shoppingpage.getCardTitle()
        i = -1
        for product in products:
            i = i+1
            productname = product.text
            log.info(productname)
            if productname == "Blackberry":
                shoppingpage.getCardFooter()[i].click()

        confirmpage = shoppingpage.getCheckout()
        shipping = confirmpage.ConfirmButton()
        log.info("Entering country name")
        shipping.countryname().send_keys("ind")
        self.linkpresence()
        shipping.countrycnfrm().click()
        shipping.checkbox().click()
        shipping.purchase_button().click()
        sent = shipping.confirm_message().text
        log.info("text received "+sent)
        assert "Success! Thank you!" in sent
        print("Successfully finished")
        
