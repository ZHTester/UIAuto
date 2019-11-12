# encoding: utf-8

"""
# @Time    : 2019-08-21 10:43
# @Author  : Function
# @FileName    : aibetCase_ios.py
# @Software: PyCharm

娱乐端 ios
"""
import datetime
import time

from AutoUI.KeyWord.GetData import Getda
from AutoUI.Util.AppiumServer import Serappium
from AutoUI.KeyWord.ActionMe import ActionMe
from AutoUI.Config.setting import *

class RunMethodIos:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_ios(driver_name,appname,sheetN,file_path=None):
        total_count = [] # 总数
        data = Getda(sheetN,file_path)
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe(driver_name,appname,sheetN)
        caselines = data.get_case_lines()
        start = datetime.datetime.now()
        print("------------start time  used---------------:",start)
        # 运行脚本
        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值

                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                print('--------------执行到行数----------------',i)
                time.sleep(2)
                excute_method(i,handle_value)
                action_method.ScreenShot(i,handle_value,file_s='../Image/Ios_img/执行图片/')
                total_count.append(i)

        end = datetime.datetime.now()
        print("------------Time used---------------:", end - start)
        total = len(total_count)
        return total



if __name__ == "__main__":
    run = RunMethodIos()
    run.run_method_ios(driver_name='ios', appname=app_name_ios_aibet, sheetN=0)
