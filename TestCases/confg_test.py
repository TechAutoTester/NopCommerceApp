from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options as opt
options=opt()
options.ignore_local_proxy_environment_variables()
serv_obj = Service(ChromeDriverManager().install())

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=serv_obj,options=options)
    return driver


