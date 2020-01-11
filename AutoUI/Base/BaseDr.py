# encoding: utf-8

"""
# @Time    : 2019-08-20 18:45
# @Author  : Function
# @FileName    : BaseDr.py
# @Software: PyCharm

获取对应的Driver
"""
import os
import time

from appium import webdriver
# from selenium import webdriver

from AutoUI.Util.WriteYaml import WriteYamlCommand
from Util.AppiumServer import Serappium
from Util.CheckPort import Cport
"""
{
  "platformName": "iOS",
  "platformVersion": "12.1.3",
  "deviceName": "windy",
  "automationName": "XCUiTest",
  "udid": "97ba21de6087bf9d34f7514df5185d86780210e5",
  "xcodeSigningId": "iPhone Develope",
  "updatedWDABundleId": "com.function.wda.lib",
  "app": "/Users/function/Downloads/UIAutioPage/BBSport.ipa",
  "xcodeOrgId": "33KMWQ75ZV",
  "bundleid": "com.bb1.sportApp0"
}
"""

class BaDriver:
    def get_ios_driver(self,app_name):
        """
        Ios Driver
        :return:
        """
        global port, capabilities
        write_file = WriteYamlCommand()
        Num = write_file.get_file_lines()
        devices_name = write_file.get_value('user_info_' + str(0), 'deviceName')
        port = write_file.get_value('user_info_' + str(0), 'port')
        capabilities = {
            "automationName": "XCUITest",
            "platformName": "iOS",
            'newCommandTimeout': "2000",
            "platformVersion": "12.4",
            "deviceName": "iPhone Xʀ",
            "app": '../Base/webDriver/' + app_name
            }

        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        return driver


    @staticmethod
    def get_android_driver(appname,i_num):
        """
        android Driver
        :return:
        """
        global port, capabilities, devices_name
        write_file = WriteYamlCommand()
        devices_name = write_file.get_value('user_info_' + str(i_num), 'deviceName')
        port = write_file.get_value('user_info_' + str(i_num), 'port')
        systemPort = write_file.get_value('user_info_' + str(i_num), 'systemPort')

        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": devices_name,
            "udid": devices_name,
            "systemPort": systemPort[i_num],
            "noReset":True,
            'newCommandTimeout': "10",
            "app": '../Base/webDriver/' + appname
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        return driver

    def main_driver(self,name,app_name,i_num):
        """
        driver 任意选择
        :param deviceName:
        :param name:
        :param app_name:
        :return:
        """
        if name == 'ios':
            res = self.get_ios_driver(app_name)
        elif name == 'android':
            res = self.get_android_driver(app_name,i_num)
        else:
            res = "没有所存在的驱动，请重新尝试"
        return res


if __name__ == '__main__':
    b = BaDriver()
    server = Serappium()
    server.main()  # 启动appium服务
    b.get_ios_driver('aibet.app')




