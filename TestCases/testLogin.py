import pytest
from TestCases.confg_test import setup
from PageObjects.loginPage import login
from Utilities.readProperties import readConfig
from Utilities.customLogger import logGen
class test_001_login:
    baseUrl = readConfig.getApplicationUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger=logGen.loggen()

    def test_Homepage_title(self,setup):
        self.driver=setup
        self.logger.info("*********test_Homepage_title test***********")
        self.logger.info("*********Verifying Homepage title***********")
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Homepage title test passed ******** ")
        else:
            self.driver.save_screenshot(".\\Screenshots"+"test_Homepage_title.png")
            self.driver.close()
            self.logger.error("************ Homepage title test failed *************")
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.logger.info("*********** Verifying Logintest ******************")
        self.driver.get(self.baseUrl)
        self.lp=login(setup)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************** Logintest passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots"+"test_login.png")
            self.driver.close()
            self.logger.error("************ Logintest failed ************")
            assert False
        self.lp.clickLogout()



