# encoding: utf-8

"""
# @Time    : 2019-08-20 18:45
# @Author  : Function
# @FileName    : BaseDr.py
# @Software: PyCharm

获取对应的Driver
"""
from appium import webdriver as H5
from selenium import webdriver as web

from Util.WriteYaml import WriteYamlCommand


class BaDriver:
    @staticmethod
    def get_web_driver():
        """
        获取浏览器 web Driver
        :return:
        """
        path = "../Base/webDriver/chromedriver"
        driver = web.Chrome(path)
        driver.maximize_window()
        driver.get("http://www.aalgds.com/login/?type=login")
        driver.implicitly_wait(1)
        return driver

    @staticmethod
    def get_web_H5():
        """
        获取浏览器 H5 Driver
        :return:
        """
        global port, devices_name
        write_file = WriteYamlCommand()
        Num = write_file.get_file_lines()
        devices_name = write_file.get_value('user_info_' + str(1), 'deviceName')
        port = write_file.get_value('user_info_' + str(1), 'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices_name,
            "platformVersion": "9",
            'noReset': 'true',
            "browserName": "Chrome",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            "sessionOverride": "true",
            "appActivity": ".BrowserActivity"
        }
        driver = H5.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        driver.get("http://m.aalgds.com/")
        return driver


    def main_driver(self,name):
        """
        driver 任意选择
        :param name:
        :return:
        """
        if name == 'web':
            res = self.get_web_driver()
            return res
        if name == 'H5':
            res = self.get_web_H5()
            return res
        else:
            res = "没有所存在的驱动，请重新尝试"
            return res


if __name__ == '__main__':
    b = BaDriver()




