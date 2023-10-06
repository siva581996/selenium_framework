import pytest
from selenium.webdriver.support.select import Select

from Testdata.Testgetdata import HomePageData
from pageobjects.Homepage import Homepage
from utilities.Basecls import Basecls


class TestFormFill(Basecls):
    def test_formfill(self, getdata):
        home = Homepage(self.driver)
        log = self.getLogger()
        home.insert_name().send_keys(getdata["firstname"])
        log.info("Entering first name as "+getdata["firstname"])
        home.insert_email().send_keys(getdata["email"])
        log.info("Entering email as "+getdata["email"])
        home.insert_pwd().send_keys(getdata["password"])
        home.ice().click()
        sel = Select(home.gend())
        sel.select_by_visible_text(getdata["gender"])
        log.info("Entering gender as "+getdata["gender"])
        home.gend()
        home.status().click()
        home.submit()
        txt = home.texted()
        log.info("Text received from the page"+txt)
        assert "Success!" in txt
        self.driver.refresh()
        print(home.pri())

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getdata(self, request):
        return request.param


