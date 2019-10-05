# encoding: utf-8

"""
# @Time    : 2019-08-20 18:45
# @Author  : Function
# @FileName    : BaseDr.py
# @Software: PyCharm

获取对应的Driver
"""

from selenium import webdriver

class BaDriver:
    @staticmethod
    def get_web_driver():
        """
        获取浏览器 web Driver
        :return:
        """
        path = "../Base/webDriver/chromedriver"
        driver = webdriver.Chrome(path)
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
        pass


    def main_driver(self,name):
        """
        driver 任意选择
        :param name:
        :return:
        """
        if name == 'web':
            res = self.get_web_driver()
        else:
            res = "没有所存在的驱动，请重新尝试"
        return res


if __name__ == '__main__':
    b = BaDriver()




