# encoding: utf-8

"""
# @Time    : 2019-08-21 10:42
# @Author  : Function
# @FileName    : ActionMethod.py
# @Software: PyCharm

关键字模型方法类
"""
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from AutoIOS.Base.BaseDriver import BaDriver
from AutoIOS.Util.GetByLocal import GetByLo
from AutoIOS.KeyWord.GetData import Getda
from AutoIOS.Config.aibet_setting import screen_images_error, screen_images_success


class ActionMe:
    def  __init__(self):
        Basedriver = BaDriver()
        self.driver = Basedriver.get_ios_driver()
        self.agetbylo = GetByLo(self.driver)
        self.agetdata = Getda()

    def GetElement(self, *args):
        """
        判断元素是否存在
        :param args:
        :return:
        """
        flag = None
        if '>' in str(args[0]):
            value = str(args[0]).split('>')
            value1 = int(value[0])
            expect_element = self.agetdata.get_expect_element(value1)  # 获取预期元素
        else:
            expect_element = self.agetdata.get_expect_element(int(args[0]))  # 获取预期元素

        by = expect_element.split(">")[0]
        by_local = expect_element.split('>')[1]

        try:
            if by == 'xpath':
                self.driver.find_element_by_xpath(by_local)
            elif by == 'classname':
                self.driver.find_element_by_class_name(by_local)
            elif by == 'css':
                self.driver.find_element_by_css_selector(by_local)
            elif by == 'id':
                self.driver.find_element_by_id(by_local)
            flag = 1
        except NoSuchElementException:
            flag = 0
        finally:
            return flag

    def JudgeSealElement(self, *args):
        """
        判断封盘元素是否存在如果不存在就等待N秒 - 如果存在就直接进入下一步
        :param args:
        :return:
        """
        flag = None
        if '>' in str(args[0]):
            value = str(args[0]).split('>')
            value1 = int(value[0])
            expect_element = self.agetdata.get_element_key(value1)
        else:
            expect_element = self.agetdata.get_element_key(int(args[0]))
        by = expect_element.split(">")[0]
        by_local = expect_element.split('>')[1]

        while flag is not 1:
            try:
                if by == 'xpath':
                    self.driver.find_element_by_xpath(by_local)
                elif by == 'classname':
                    self.driver.find_element_by_class_name(by_local)
                elif by == 'css':
                    self.driver.find_element_by_css_selector(by_local)
                elif by == 'id':
                    self.driver.find_element_by_id(by_local)
                flag = 0
                time.sleep(120)
                continue
            except NoSuchElementException:
                break

    def Input(self,*args):
        """
        输入值方法
        :return:
        """
        value = str(args[0]).split('>')
        value1 = int(value[0])
        value2 = value[1]
        element = self.agetbylo.get_element(value1)
        if element is None:
            return '', "元素没找到"
        element.send_keys(value2)

    def OnClick(self, *args):
        """
        点击操作方法
        :return:

        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        element.click()

    def GetPerform(self, *args):
        """
         坐标定位点击操作
        :return:
        """
        value = str(args[0]).split('>')
        X = int(value[1])
        Y = int(value[2])
        TouchAction(self.driver).press(x=X, y=Y).release().perform()

    def Yingc(self, *args):
        """
        IOS隐藏键盘
        :param args:
        :return:
        """
        self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()

    def ScreenShot(self, *args):
        """
        截图方法
        :return:
        """
        if '>' in  str(args[0]):
            value = str(args[0]).split('>')
            value1 = int(value[0])
            imageName = str('ID' + str(value1) + self.agetdata.get_caseName(value1))
            self.driver.get_screenshot_as_file(screen_images_success + imageName + '.png')
        else:
            i = int(args[0])
            imageName = str('ID' + str(i) +self.agetdata.get_caseName(i))
            self.driver.get_screenshot_as_file(screen_images_success + imageName + '.png')

    def ScreenShotError(self, *args):
        """
        错误异常截图方法
        :return:
        """
        if '>' in  str(args[0]):
            value = str(args[0]).split('>')
            value1 = int(value[0])
            imageName = str(self.agetdata.get_caseName(value1))
            self.driver.get_screenshot_as_file(screen_images_error + imageName + '.png')
        else:
            i = int(args[0])
            imageName = str('ID' + str(i) +self.agetdata.get_caseName(i))
            self.driver.get_screenshot_as_file(screen_images_error + imageName + '.png')

    def GetiPhoneCode(self,*args):
        """
        此处是需要调用接口的 整体调试的时候加上该接口
        :return:
        """
        pass

    def GetTostElement(self,*args):
        """
        获取tost元素 SwitchTo
        1 原生APP切换到H5
        2 H5切换到APP
        :return:
        """
        pass

    def ios_SwipeRight(self):
        """
        ios滑动 右边
        :return:
        """
        self.driver.execute_script("mobile:scroll", {"direction": "right"})

    def ios_SwipeLeft(self, *args):
        """
        ios滑动 左边
        :return:
        """
        self.driver.execute_script("mobile:scroll", {"direction": "left"})

    def ios_SwipeUp(self,*args):
        """
        ios滑动 上
        :return:
        """
        self.driver.execute_script("mobile:scroll", {"direction": "up"})

    def ios_SwipeDown(self,*args):
        """
        ios滑动  下
        :return:
        """
        self.driver.execute_script("mobile:scroll", {"direction": "down"})

    def SleepTime(self, *args):
        """
        停止时间
        :param args:
        :return:
        """
        if '>' in  str(args[0]):
            value = str(args[0]).split('>')
            value1 = int(value[1])
            time.sleep(int(value1))
        else:
            time.sleep(int(args[0]))

    def get_size(self, *args):
        """
        Android获取屏幕高宽和高
        :param args:
        :return:
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self, *args):
        """
        Android向左边滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    def swipe_right(self, *args):
        """
        Android向右边滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    def swipe_up(self, *args):
        """
        Android向上滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10 * 2
        self.driver.swipe(x1, y1, x1, y, 1000)

    def swipe_down(self, *args):
        """
        Android向下滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)



if __name__ == '__main__':
    pass
