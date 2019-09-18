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
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException

from AutoUI.Base.BaseDriver import BaDriver
from AutoUI.Util.GetByLocal import GetByLo
from AutoUI.KeyWord.GetData import Getda
from AutoUI.Config.aibet_setting import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ActionMe:
    def  __init__(self,filepath,driver_name,appname):
        Basedriver = BaDriver()
        self.driver = Basedriver.main_driver(driver_name,appname)
        self.agetbylo = GetByLo(self.driver,filepath)
        self.agetdata = Getda(filepath)

    def GetElement(self, *args):
        """
        判断元素是否存在
        :param args:
        :return:
        """
        flag = None
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
                time.sleep(5)
                continue
            except NoSuchElementException:
                break

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

    def CAlert(self, *args):
        """
        ios 系统弹出默认alert框
        :return:
        """
        self.driver.switch_to.alert.accept()

    def GetPerform(self, *args):
        """
         坐标定位点击操作
        :return:
        """
        value = str(args[1]).split('>')
        X = int(value[0])
        Y = int(value[1])
        TouchAction(self.driver).press(x=X, y=Y).release().perform()

    def Yingc(self, *args):
        """
        IOS隐藏键盘
        :param args:
        :return:
        """
        try:
            self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        except NoSuchElementException:
            print('---------页面元素找不到键盘元素-------------')

    def ScreenShot(self, *args):
        """
        截图方法
        :return:
        """
        i = int(args[0])
        imageName = str('ID' + str(i) +self.agetdata.get_caseName(i))
        self.driver.get_screenshot_as_file(screen_images_success + imageName + '.png')

    def ScreenShotError(self, *args):
        """
        错误异常截图方法
        :return:
        """
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
        flag = None
        expect_element = self.agetdata.get_expect_element(int(args[0]))  # 获取预期元素
        by = expect_element.split(">")[0]
        by_local = expect_element.split('>')[1]
        try:
            toElement = (by, by_local)
            WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toElement))
            flag = 1
        except NoSuchElementException:
            flag = 0
        finally:
            return flag

    def lun_Image(self,inter):
        imageName = str('ID' + str(inter) +self.agetdata.get_caseName(inter))
        self.driver.get_screenshot_as_file( lun_image + imageName + '.png')

    def lunActivity(self,*args):
        """
        循环获得活动元素
        :return:
        """
        for inter in range(1,5):
            try:
                xpath1, xpath2 = self.agetbylo.get_lun_element(int(args[0]))
                xpath1 = xpath1.format(inte=inter)
                self.driver.find_element_by_xpath(xpath1).click()
                time.sleep(3)
                imageName = str('ID' + str(inter) + '循环轮播图')
                self.driver.get_screenshot_as_file(lun_image + imageName + '.png')
                time.sleep(1)
                self.driver.find_element_by_xpath(xpath2).click()
                self.swipe_up_lunbo()
            except NoSuchElementException:
                print('-------没有图片了----------')
            finally:
                self.ios_SwipeDown()

    def swipe_up_lunbo(self, *args):
        """
        Android向上滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 5
        y = self.get_size()[1] / 10 * 8
        self.driver.swipe(x1, y1, x1, y, 1000)

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

    def ChoiceData(self,*args):
        """
        :param args:
        :return:
        日期选择
        """
        xx = str(args[1]).split(">")
        x = int(xx[0])
        y = int(xx[1])
        x1 = int(xx[2])
        y1 = int(xx[3])
        times = int(xx[4])
        self.driver.swipe(x, y, x1, y1,times)

    def ios_SwipeRight(self,*args):
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

    @staticmethod
    def SleepTime(*args):
        """
        停止时间
        :param args:
        :return:
        """
        time.sleep(int(args[1]))

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
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y, 1000)

    def swipe_down(self, *args):
        """
        Android向下滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10 * 7
        self.driver.swipe(x1, y1, x1, y, 1000)



if __name__ == '__main__':
    pass
