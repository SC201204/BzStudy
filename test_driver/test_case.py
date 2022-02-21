# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     test_case
# Author:       SGQ
# Datetime:    2022-02-21 13:45
# Description：
# -----------------------------------------------------------------------------------
import time

import pytest
from selenium.webdriver.common.by import By


class TestCase:


    @pytest.mark.parametrize("value", [("selenium",), ("python",)])
    def test_kw(self, get_driver, value):
        get_driver.get("https://www.baidu.com")
        get_driver.find_element(By.ID, "kw").send_keys(value)
        get_driver.find_element(By.ID,"su").click()
        get_driver.find_element(By.ID, "kw").clear()
        time.sleep(4)

    @pytest.mark.parametrize("value", [("selenium1",), ("python1",)])
    def test_kw1(self, get_driver, value):
        get_driver.get("https://www.baidu.com")
        get_driver.find_element(By.ID, "kw").send_keys(value)
        get_driver.find_element(By.ID, "su").click()
        get_driver.find_element(By.ID, "kw").clear()
        time.sleep(4)