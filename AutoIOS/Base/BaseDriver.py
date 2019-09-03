# encoding: utf-8

"""
# @Time    : 2019-08-20 18:45
# @Author  : Function
# @FileName    : BaseDriver.py
# @Software: PyCharm

获取对应的Driver
"""
import warnings
from appium import webdriver
import time

from AutoIOS.Util.WriteYaml import WriteYamlCommand
from AutoIOS.Config.aibet_setting import app_name


class BaDriver:
    @staticmethod
    def get_ios_driver():
        """
        ios Driver
        :return:
        """
        write_file = WriteYamlCommand()
        port = write_file.get_value('port')
        capabilities = {
            "automationName": "XCUITest",
            "platformName": "iOS",
            'newCommandTimeout': "2000",
            "platformVersion": "12.4",
            "deviceName": "iPhone Xs Max",
            "app": "/Users/function/Downloads/UIAutioPage/"+app_name
                                    }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        return driver

    def get_android_driver(self):
        """
        android Driver
        :return:
        """
        pass




if __name__ == '__main__':
    dr = BaDriver()
    dr.get_ios_driver()


