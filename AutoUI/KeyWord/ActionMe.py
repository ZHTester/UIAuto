# encoding: utf-8
"""
# @Time    : 2019-08-21 10:42
# @Author  : Function
# @FileName    : ActionMe.py
# @Software: PyCharm

移动端API
"""
import random
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from AutoUI.Base.BaseDr import BaDriver
from AutoUI.Util.GetByLocal import GetByLo
from AutoUI.KeyWord.GetData import Getda
from AutoUI.Config.setting import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutoUI.Util.OtherFunction import creatFile


class ActionMe:
    def  __init__(self,driver_name,sheetN,i_num,appname=None,file_path=None):
        Basedriver = BaDriver()
        self.driver = Basedriver.main_driver(driver_name,appname,i_num)
        self.agetbylo = GetByLo(self.driver,sheetN,file_path)
        self.agetdata = Getda(sheetN)

    ##############################体育部分从这开始#######################################

    def ClickElement(self, *args):
        """
        元素点击
        :param args:
        :return:
        """
        global tmp
        element = self.agetdata.get_element_key(int(args[0]))
        by = element.split("<")[0]
        by_local = element.split('<')[1]
        try:
            if by == 'xpath':
                tmp = self.driver.find_element_by_xpath(by_local)
            elif by == 'classname':
                tmp = self.driver.find_element_by_class_name(by_local)
            elif by == 'css':
                tmp = self.driver.find_element_by_css_selector(by_local)
            elif by == 'id':
                tmp = self.driver.find_element_by_id(by_local)
            elif by == 'aid':
                tmp = self.driver.find_element_by_id(by_local)
            elif by == 'link_text':
                tmp = self.driver.find_element_by_link_text(by_local)
            tmp.click()
            time.sleep(1)
        except NoSuchElementException:
            print('元素不存在')

    def findElements(self, *args):
        """
        元素点击
        :param args:
        :return:
        """
        global tmp
        element = self.agetdata.get_element_key(int(args[0]))
        # by = element.split("<")[0]
        by_local = element.split('<')[1]
        try:
            tmp = self.driver.find_elements_by_class_name(by_local)
            if len(tmp) >= 4:
                print("赛事多于两场，可以进行串关投注")
                return "ok"
            else:
                print("赛事小于两场，不能进行串关投注")
                return "no"
        except NoSuchElementException:
            print('元素不存在')

    def move(self, *args):
        """
        滑动
        :return:
        """
        offset = args[1]
        postion = offset.split("<")
        start_x = postion[0]
        start_y = postion[1]
        end_x = postion[2]
        end_y = postion[3]
        print(start_x, start_y, end_x, end_y)
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y)
        except Exception as e:
            print("发生异常:" + str(e))

    def toWebview(self, *args):
        """
        跳转到webview
        :return:
        """
        value = str(args[1])
        self.driver.switch_to.context(value)

    def toNative(self, *args):
        """
        跳转到app
        :return:
        """
        self.driver.switch_to.context("NATIVE_APP")

    def pclick(self, *args):
        """
        坐标点击
        :return:
        """
        pass
        element = args[1]
        postion = element.split("<")
        x = postion[0]
        y = postion[1]
        if element is None:
            return '', "未读取到坐标"
        # print(element,type(element))
        ActionChains(self.driver).move_by_offset(x, y).click().perform()

##############################体育部分在这结束#######################################

    def JudgeSealElement(self, *args):
        """
        判断封盘元素是否存在如果不存在就等待N秒 - 如果存在就直接进入下一步
        :param args:
        :return:
        """
        flag = None
        expect_element = self.agetdata.get_element_key(int(args[0]))
        by = expect_element.split("<")[0]
        by_local = expect_element.split('<')[1]

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

    def CreatePhone(self, *args):
        """
        随机生成手机号 发送操作
        :param args:
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"

        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        phone_Number ="1{}{}{}".format(second, third, suffix)
        element.send_keys(phone_Number)

    def Clear(self,*args):
        """
        清空输入框
        :param args:
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        element.clear()

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
        try:
            value = str(args[1]).split('<')
            X = int(value[0])
            Y = int(value[1])
            TouchAction(self.driver).press(x=X, y=Y).release().perform()
        except Exception as e:
            print('******找不到坐标*****',int(args[0]))

    def Ten(self, *args):
        """
         坐标定位点击操作
        :return:
        """
        try:
            value = str(args[1]).split('<')
            X = int(value[0])
            Y = int(value[1])
            for i in range(10):
                TouchAction(self.driver).press(x=X, y=Y).release().perform()
        except Exception as e:
            print('******找不到坐标*****',int(args[0]))


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

    def ScreenShot(self, *args,file_s=None):
        """
        截图方法
        :return:
        """
        i = int(args[0])
        imageName = str('ID' + str(i) +self.agetdata.get_caseName(i))
        file_path = creatFile(file_s)
        self.driver.get_screenshot_as_file(file_path + imageName + '.png')

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
        by = expect_element.split("<")[0]
        by_local = expect_element.split('<')[1]
        try:
            toElement = (by, by_local)
            WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toElement))
            flag = 1
        except NoSuchElementException:
            flag = 0
        finally:
            return flag

    def lun_Image(self,inter):
        imageName = str('ID' + str(inter) + self.agetdata.get_caseName(inter))
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
                time.sleep(8)
                imageName = str('ID' + str(inter) + '循环轮播图')
                self.ScreenShot()
                time.sleep(1)
                self.driver.find_element_by_xpath(xpath2).click()
                self.swipe_up_lunbo(str(args[0]))
            except NoSuchElementException:
                print('-------没有图片了----------')
            finally:
                self.swipe_up_lunbo(str(args[0]))

    def swipe_up_lunbo(self, *args):
        name = str(args[0])
        if name == 'ios':
            self.ios_SwipeDown()
        else:
            self.swipe_down()

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
        xx = str(args[1]).split("<")
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
        y1 = self.get_size()[1] / 10 * 5
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y,1000)

    def swipe_down(self, *args):
        """
        Android向下滑动
        :param args:
        :return:
        """
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10 * 5
        self.driver.swipe(x1, y1, x1, y, 1000)

"""
=================================--------------appium------------------==========================
"""


if __name__ == '__main__':
    pass
