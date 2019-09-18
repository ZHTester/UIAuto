# encoding: utf-8

"""
# @Time    : 2019-08-20 18:45
# @Author  : Function
# @FileName    : BaseDriver.py
# @Software: PyCharm

获取对应的Driver
"""
from appium import webdriver

from AutoUI.Util.WriteYaml import WriteYamlCommand


class BaDriver:
    @staticmethod
    def get_ios_driver(app_name):
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
            "app": "/Users/function/Downloads/UIAutioPage/" + app_name
              }

        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        print('-------123-----',driver)
        return driver

    @staticmethod
    def get_android_driver(appname):
        """
        android Driver
        :return:
        """
        write_file = WriteYamlCommand()
        port = write_file.get_value('port')
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "192.168.56.102:5555",
            "app": "/Users/function/Downloads/UIAutioPage/" + appname
        }

        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)

        return driver

    def main_driver(self,name,app_name):
        """
        driver 任意选择
        :param name:
        :param app_name:
        :return:
        """
        if name == 'ios':
            res = self.get_ios_driver(app_name)
        elif name == 'android':
            res = self.get_android_driver(app_name)
        else:
            res = "没有所存在的驱动，请重新尝试"
        return res





if __name__ == '__main__':
    b = BaDriver()
    b.main_driver('android')




