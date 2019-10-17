# encoding: utf-8
"""
# @Time    : 2019-09-16 16:28
# @Author  : Function
# @FileName    : aibetCase_android.py
# @Software: PyCharm

娱乐端  android
"""
import datetime
import time

from AutoUI.KeyWord.GetData import Getda
from AutoUI.Util.AppiumServer import Serappium
from AutoUI.KeyWord.ActionMe import ActionMe
from AutoUI.Util.SendEmail import SEmail
from AutoUI.Config.setting import *


class RunMethodAndroid:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_adnroid(driver_name,appname,sheetN):
        pass_count = []  # 统计成功个数
        total_count = []  # 总数
        data = Getda(sheetN)
        server = Serappium()
        server.main()  # 启动appium服务
        action_method = ActionMe(driver_name, appname, sheetN)
        caselines = data.get_case_lines()
        start = datetime.datetime.now()
        print("------------start time  used---------------:", start)

        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值
                result_test = data.get_is_result(i)  # 获取结果

                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                print('-------------------------------', i)
                time.sleep(2)
                excute_method(i, handle_value)
                action_method.ScreenShot(i, handle_value, file_s='../Image/android_img/执行图片/')
                total_count.append(i)
                # 判断预期元素在当前页面是否存在
                if result_test != "测试失败":
                    data.write_value(i, '测试通过',sheetN)
                    pass_count.append(i)

        end = datetime.datetime.now()
        pass_count_num = len(pass_count)
        fail_count_num = len(total_count) - len(pass_count)
        print("------------Time used---------------:", end - start)

        return pass_count_num, fail_count_num

if __name__ == "__main__":
    run = RunMethodAndroid()
    run.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1)





