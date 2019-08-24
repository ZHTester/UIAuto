# encoding: utf-8

"""
# @Time    : 2019-08-21 10:42
# @Author  : Function
# @FileName    : ActionMethod.py
# @Software: PyCharm

关键字模型方法类
"""
import time

from aibetPr.Base.BaseDriver import BaDriver
from aibetPr.Util.GetByLocal import GetByLo
from aibetPr.KeyWord.GetData import Getda



class ActionMe:
    def  __init__(self):
        Basedriver = BaDriver()
        self.driver = Basedriver.get_ios_driver()
        self.agetbylo = GetByLo(self.driver)
        self.agetdata = Getda()
        self.rows = self.agetdata.get_rowi()

    def Input(self,*args):
        """
        输入值方法
        :return:
        """
        value = str(args[0]).split(',')
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

    def ScreenShot(self, *args):
        """
        截图方法
        :return:
        """
        imageName = str(self.agetdata.get_caseName(args[0]))
        self.driver.get_screenshot_as_file(r'../ScreenImages/'+imageName+'.png')

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

    def Ios_hide_keyboard(self,*args):
        """
        IOS隐藏键盘
        :param args:
        :return:
        """
        self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()

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

    def SleepTime(self, *args):
        """
        停止时间
        :param args:
        :return:
        """
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