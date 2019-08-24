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
from aibetPr.Util.WriteYaml import WriteYamlCommand


class BaDriver:
    @staticmethod
    def get_ios_driver():
        """
        ios Driver
        :return:
        """
        warnings.simplefilter("ignore", ResourceWarning)  # 不打印系统报错
        write_file = WriteYamlCommand()
        port = write_file.get_value('port')
        print(port)
        capabilities = {
            "automationName": "XCUITest",
            "platformName": "iOS",
            "platformVersion": "12.4",
            "deviceName": "iPhone Xʀ",
            "app": "/Users/function/Downloads/UIAutioPage/aibet.app"
                                    }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        # driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        # driver.switch_to.alert.dismiss()
        # driver.execute_script("mobile:scroll", {"direction":"right"})
        # driver.find_elements_by_ios_predicate("type=='XCUIElementTypeOther'  AND name=='http://m.aalgds.com'")  # 元素信息定位
        time.sleep(5)
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


