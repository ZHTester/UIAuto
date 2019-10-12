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
from AutoUI.Util.SendEmail import SEmail
from AutoUI.Util.ImageZip import make_zip
from AutoUI.Util.OtherFunction import pass_fail_number
from AutoUI.Config.setting import *

class RunMethodIos:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_ios(driver_name,appname,sheetN):
        pass_count = []  # 统计成功个数
        fail_count =[]  # 统计失败个数
        data = Getda(sheetN)
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe(driver_name,appname,sheetN)
        caselines = data.get_case_lines()
        start = datetime.datetime.now()
        print("------------start time  used---------------:",start)
        print("------------start time  used---------------:",start)
        # 注视 注视 注视
        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值
                expect_step = data.get_expect_handle(i)  # 预期元素操作步骤

                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                print('-------------------------------', i)
                time.sleep(1)
                excute_method(i,handle_value)
                action_method.ScreenShot(i,handle_value,file_s='../Image/Ios_img/执行图片/')

                # 判断预期元素在当前页面是否存在
                if expect_step is not None:
                    expect_result = getattr(action_method, expect_step)
                    result = expect_result(i, handle_value)
                    if result == 1:
                        data.write_value(i, '测试通过')
                        pass_count.append(i)
                    else:
                        data.write_value(i, '测试失败')
                        fail_count.append(i)
        end = datetime.datetime.now()
        print("------------Time used---------------:", end - start)

        return [pass_count,fail_count]


if __name__ == "__main__":
    run = RunMethodIos()
    run.run_method_ios(driver_name='ios', appname=app_name_ios_aibet, sheetN=0)
