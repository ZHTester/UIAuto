# encoding: utf-8

"""
# @Time    : 12/11/2019 4:20 下午
# @Author  : Function
# @FileName    : demo0001.py
# @Software: PyCharm
"""

import datetime
import time

from AutoUI.KeyWord.GetData import Getda
from AutoUI.Util.AppiumServer import Serappium
from AutoUI.KeyWord.ActionMe import ActionMe
from KeyWord.ActionMe_Selenium import ActionMeSelenium
from AutoUI.Util.SendEmail import SEmail
from AutoUI.Config.setting import *


class RunMethodAll:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_All(driver_name,sheetN,Run_name,i_num,appname=None,time_sleep=None):
        global action_method, action_method_selenium
        total_count = []  # 总数
        pass_count = []
        data = Getda(sheetN)
        if Run_name == 'ios':
            action_method = ActionMe(driver_name, sheetN,i_num,appname)
        elif Run_name == 'android':
            action_method = ActionMe(driver_name, sheetN,i_num,appname)
        elif Run_name == 'H5':
            action_method_selenium = ActionMeSelenium(driver_name, sheetN)
        elif Run_name == 'web':
            action_method_selenium = ActionMeSelenium(driver_name, sheetN)

        caselines = data.get_case_lines()
        start = datetime.datetime.now()
        print("------------start time  used---------------:", start)
        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值
                # 自动化测试用例集执行
                if Run_name == 'android':
                    excute_method = getattr(action_method, handle_step)
                    print('--------------{0}--****************----执行到行数-------------------------'.format(sheetN), i)
                else:
                    excute_method = getattr(action_method_selenium, handle_step)
                    print('--------------{0}--*******8888888*********----执行到行数-------------------------'.format(sheetN), i)

                time.sleep(time_sleep)
                excute_method(i, handle_value)

                if Run_name == 'android':
                    action_method.ScreenShot(i, handle_value, file_s='../Image/'+Run_name+'/执行图片/')
                else:
                    action_method_selenium.ScreenShot(i, handle_value, file_s='../Image/'+Run_name+'/执行图片/')

                total_count.append(i)

                result_test = data.get_is_result(i)  # 获取结果
                # # 判断预期元素在当前页面是否存在
                # if result_test != '测试失败':
                #     data.write_value(i, "测试通过")
                #     pass_count.append(i)

        end = datetime.datetime.now()
        print("------------Time used---------------:", end - start)

        total = len(total_count)
        return total

if __name__ == "__main__":
    run = RunMethodAll()
    run.run_method_All(driver_name='android',  sheetN=1, Run_name='android',appname="ballbet.apk")
    run.run_method_All(driver_name='web',sheetN=2,Run_name='web')
    # run.run_method_All(driver_name='H5', sheetN=3,Run_name='H5')






