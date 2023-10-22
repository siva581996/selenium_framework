import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setups")
class Basecls:
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("/home/sivakumar/PycharmProjects/sele2e/utilities/'logfiles.log'")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def linkpresence(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))


    