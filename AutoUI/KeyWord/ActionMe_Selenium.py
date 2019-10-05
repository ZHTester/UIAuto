# encoding: utf-8

"""
# @Time    : 2019-10-05 11:23
# @Author  : Function
# @FileName    : ActionMe_Selenium.py
# @Software: PyCharm
web H5 相关api
"""
import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from AutoUI.Base.BaseDr_Selenium import BaDriver
from AutoUI.Util.GetByLocal import GetByLo
from AutoUI.KeyWord.GetData import Getda
from Util.OtherFunction import creatFile


class ActionMe:
    def  __init__(self,driver_name,sheetN):
        Basedriver = BaDriver()
        self.driver = Basedriver.main_driver(driver_name)
        self.agetbylo = GetByLo(self.driver,sheetN)
        self.agetdata = Getda(sheetN)

    def GetElement(self, *args):
        """
        判断元素是否存在
        :param args:
        :return:
        """
        flag = None
        expect_element = self.agetdata.get_expect_element(int(args[0]))  # 获取预期元素
        by = expect_element.split("<")[0]
        by_local = expect_element.split('<')[1]
        try:
            if by == 'xpath':
                self.driver.find_element_by_xpath(by_local)
            elif by == 'classname':
                self.driver.find_element_by_class_name(by_local)
            elif by == 'css':
                self.driver.find_element_by_css_selector(by_local)
            elif by == 'id':
                self.driver.find_element_by_id(by_local)
            elif by == 'aid':
                return self.driver.find_element_by_id(by_local)
            flag = 1
        except NoSuchElementException:
            flag = 0
        finally:
            return flag

    def Input(self,*args):
        """
        输入值方法
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        value = str(args[1])
        if '.0' in value:
            value1 = int(args[1])
            element.send_keys(value1)
        else:
            element.send_keys(value)

    def OnClick(self, *args):
        """
        点击操作方法
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        element.click()

    def Rinput(self,*args):
        """
        随机生成数字字母
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        num_set = [chr(i) for i in range(48, 58)]
        char_set = [chr(i) for i in range(97, 123)]
        total_set = num_set + char_set
        value_set = "".join(random.sample(total_set, int(args[1])))
        element.send_keys(value_set)

    def WOnClick(self, *args):
        """
        Web点击操作方法
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        else:
            element.click()
            time.sleep(3)

    def W_clear(self, *args):
        """
        清空输入框
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        else:
            text = element.get_attribute('value')
            print(text)
            for i in text:
                element.send_keys(Keys.BACKSPACE)

    def switchIframe(self, *args):
        """
        定位到iframe
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        else:
            self.driver.switch_to_frame(element)

    def switchDefault(self, *args):
        """
        跳出iframe
        :return:
        """
        self.driver.switch_to.default_content()

    def switchTab(self, *args):
        """
        切换浏览器页签
        :return:
        """
        value = int(args[1])
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[value])
        time.sleep(2)

    def scrollDown(self, *args):
        """
        页面滑动到底部
        :return:
        """
        self.driver.execute_script("window.scrollTo(0,2370)")

    def scrollUp(self, *args):
        """
        页面滑动到底部
        :return:
        """
        self.driver.execute_script("window.scrollTo(0,0)")

    @staticmethod
    def timeSleep(*args):
        """
        时间等待
        :return:
        """
        value = int(args[1])
        time.sleep(value)

    def bowserBack(self, *args):
        """
        切换浏览器页签
        :return:
        """
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def closeTab(self, *args):
        """
        跳出iframe
        :return:
        """
        time.sleep(2)
        self.driver.close()

    def pageDown(self, *args):
        """
        清空输入框
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        else:
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)

    def notice_win(self, *args):
        """
        登录弹窗
        :return:
        """
        time.sleep(2)
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        else:
            element.click()

    def ScreenShot(self, *args,file_s=None):
        """
        截图方法
        :return:
        """
        i = int(args[0])
        imageName = str('ID' + str(i) +self.agetdata.get_caseName(i))
        file_path = creatFile(file_s)
        self.driver.get_screenshot_as_file(file_path + imageName + '.png')

if __name__ == '__main__':
    pass
