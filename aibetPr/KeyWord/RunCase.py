# encoding: utf-8

"""
# @Time    : 2019-08-21 10:43
# @Author  : Function
# @FileName    : RunCase.py
# @Software: PyCharm

关键字视图方法调用
"""
import time

from aibetPr.KeyWord.GetData import Getda
from aibetPr.Util.AppiumServer import Serappium
from aibetPr.KeyWord.ActionMethod import ActionMe
from aibetPr.Util.SendEmail import SEmail


class RunMethod:
    def __init__(self):
        self.data = Getda()

    def __getattr__(self, item):
        return "excel 有空格请检查"

    def run_method(self):
        global p,f
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe()
        caselines = self.data.get_case_lines()
        sendemail = SEmail()

        for i in range(1, caselines):
            handle_step = self.data.get_handle_step(i)  # 执行方法
            handle_value = self.data.get_handle_value(i)  # 操作值
            expect_step = self.data.get_expect_handle(i)  # 预期元素操作步骤
            try:
                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                excute_method(handle_value)
                action_method.ScreenShot(handle_value)

                # 判断预期元素在当前页面是否存在
                if expect_step is not None:
                    expect_result = getattr(action_method, expect_step)
                    result = expect_result(handle_value)
                    if result:
                        self.data.write_value(i, "pass")
                    else:
                        self.data.write_value(i, "fail")
                    # 获取成功失败的统计个数 p=pass个数  f = 失败个数
                    p= self.data.getTotal(i)
                    p = str(p)
                    print(p)
                    print(type(p))
            except:
                action_method.ScreenShotError(handle_value)
        message = '娱乐端app(ios)自动化测试报告\n\n以下就是ui自动化测试报告\n成功测试用个数为:'+\
                  '\n失败测试用例个数为:\n\n 附件为本次测试用例具体执行结果'
        sendemail.Email_UiTest(message)


if __name__ == "__main__":
    run = RunMethod()
    run.run_method()
