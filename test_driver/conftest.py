# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     conftest
# Author:       SGQ
# Datetime:    2022-02-21 13:42
# Description：
# -----------------------------------------------------------------------------------
import pytest
from selenium import webdriver

@pytest.fixture(scope="class",params=["Chrome", "edge"])
# @pytest.fixture()
def get_driver(request):
    if request.param=="Chrome":
        driver =webdriver.Chrome()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    print(request.param)