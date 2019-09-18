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
from AutoUI.KeyWord.ActionMethod import ActionMe
from AutoUI.Util.SendEmail import SEmail
from AutoUI.Util.ImageZip import make_zip
from AutoUI.Util.OtherFunction import pass_fail_number, LogReport
from AutoUI.Config.aibet_setting import *


class RunMethod:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method(excle_path,appname,driver_name):
        LogReport()  # 日志记录
        pass_count = []  # 统计成功个数
        fail_count =[]  # 统计失败个数
        data = Getda(excle_path)
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe(excle_path,driver_name,appname)
        caselines = data.get_case_lines()
        sendemail = SEmail()
        start = datetime.datetime.now()
        print("------------start time  used---------------:",start)
        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值
                expect_step = data.get_expect_handle(i)  # 预期元素操作步骤

                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                action_method.ScreenShot(i,handle_value)
                excute_method(i,handle_value)
                time.sleep(2)


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

        # 打印成功失败的图片压缩文件
        make_zip(screen_images_success,images_success) # 打印成功图片成zip文件
        make_zip(screen_images_error,images_error)

        # # 结果邮件发送
        message = pass_fail_number(pass_count,fail_count,end)
        sendemail.Email_UiTest(message,aibetCase_Ios_file,OUT_FILENAME)


if __name__ == "__main__":
    run = RunMethod()
    run.run_method(aibetCase_Ios_file,app_name_ios_aibet,driver_name='ios')
