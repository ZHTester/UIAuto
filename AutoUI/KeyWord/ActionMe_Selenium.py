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
from Base.BaseDr_Selenium import BaDriver
from Util.GetByLocal import GetByLo
from KeyWord.GetData import Getda
from Util.OtherFunction import creatFile
from selenium.webdriver.common.action_chains import ActionChains

class ActionMeSelenium:
    def __init__(self,driver_name,sheetN,i_num=None):
        Basedriver = BaDriver()
        self.driver = Basedriver.main_driver(driver_name,i_num)
        self.agetbylo = GetByLo(self.driver,sheetN)
        self.agetdata = Getda(sheetN)

    def GetElement(self, *args):
        """
        判断元素是否存在
        :param args:
        :return:
        """
        global tmp
        element = self.agetbylo.get_element(int(args[0]))
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
        except NoSuchElementException:
            print('元素不存在')

    def Input(self, *args):
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

    def P_Click(self, *args):
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

    def Move(self, *args):
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

    def moveTo(self, *args):
        """
        鼠标移动到指定元素
        :return:
        """
        element = self.agetbylo.get_element(int(args[0]))
        if element is None:
            return '', "元素没找到"
        ActionChains(self.driver).move_to_element(element).perform()

    def OnClick(self, *args):
        """
        点击操作方法
        :return:
        """
        try:
            element = self.agetbylo.get_element(int(args[0]))
            if element is None:
                return '', "元素没找到"
            element.click()
            time.sleep(1)
        except Exception as e:
            print("发生异常:" + str(e))

    def getUrl(self, *args):
        """
        跳转url
        :return:
        """
        value = str(args[1])
        self.driver.get(value)

    def WaitClick(self, *args):
        """
        等待元素加载后点击
        :return:
        """
        try:
            element = self.agetbylo.get_element(int(args[0]))
            if element is None:
                return '', "元素没找到"
            element.click()
            time.sleep(3)
        except Exception as e:
            print("发生异常:" + str(e))

    def Rinput(self, *args):
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

    def clear(self, *args):
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

    def hide_Keyboard(self, *args):
        """
        隐藏键盘
        :return:
        """
        self.driver.hide_keyboard()

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
        try:
            self.driver.switch_to_window(windows[value])
            time.sleep(2)
        except Exception as e:
            print("发生异常:" + str(e))

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
        value = args[1]
        print("等待元素加载")
        time.sleep(int(value))

    def bowserBack(self, *args):
        """
        切换浏览器页签
        :return:
        """
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

    def ScreenShot(self, *args, file_s=None):
        """
        截图方法
        :return:
        """
        i = int(args[0])
        imageName = str('ID' + str(i) + self.agetdata.get_caseName(i))
        file_path = creatFile(file_s)
        self.driver.get_screenshot_as_file(file_path + imageName + '.png')


if __name__ == '__main__':
    pass
