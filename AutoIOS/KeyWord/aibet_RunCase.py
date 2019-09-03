# encoding: utf-8

"""
# @Time    : 2019-08-21 10:43
# @Author  : Function
# @FileName    : aibet_RunCase.py
# @Software: PyCharm

关键字视图方法调用
"""
import time

from AutoIOS.KeyWord.GetData import Getda
from AutoIOS.Util.AppiumServer import Serappium
from AutoIOS.KeyWord.ActionMethod import ActionMe
from AutoIOS.Util.SendEmail import SEmail
from AutoIOS.Util.ImageZip import make_zip
from AutoIOS.Util.OtherFunction import pass_fail_number, LogReport
from AutoIOS.Config.aibet_setting import *


class RunMethod:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    def run_method(self):
        LogReport()  # 日志记录
        pass_count = []  # 统计成功个数
        fail_count =[]  # 统计失败个数
        data = Getda()
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe()
        caselines = data.get_case_lines()
        sendemail = SEmail()

        for i in range(1, caselines):
            handle_step = data.get_handle_step(i)  # 执行方法
            handle_value = data.get_handle_value(i)  # 操作值
            expect_step = data.get_expect_handle(i)  # 预期元素操作步骤

            time.sleep(2)
            # 自动化测试用例集执行
            excute_method = getattr(action_method, handle_step)
            excute_method(handle_value)
            action_method.ScreenShot(handle_value)

            # 判断预期元素在当前页面是否存在
            if expect_step is not None:
                expect_result = getattr(action_method, expect_step)
                result = expect_result(handle_value)
                if result == 1:
                    data.write_value(i, '测试通过')
                    pass_count.append(i)
                else:
                    data.write_value(i, '测试失败')
                    fail_count.append(i)

        print('成功的测试用例编号:%s'% pass_count)
        print('失败的测试用例编号:%s'% fail_count)

        # 打印成功失败的图片压缩文件
        make_zip(screen_images_success,images_success) # 打印成功图片成zip文件
        make_zip(screen_images_error,images_error)

        # # 结果邮件发送
        message = pass_fail_number(pass_count,fail_count,app_name)
        sendemail.Email_UiTest(message,report_file,OUT_FILENAME)


if __name__ == "__main__":
    run = RunMethod()
    run.run_method()
