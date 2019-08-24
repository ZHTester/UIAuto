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


class RunMethod:
    def __init__(self):
        self.data = Getda()

    def __getattr__(self, item):
        return "excel 有空格请检查"

    def run_method(self):
        server = Serappium()
        server.main()  #  启动appium服务
        action_method = ActionMe()
        caselines = self.data.get_case_lines()

        for i in range(1, caselines):
            handle_step = self.data.get_handle_step(i)  # 执行方法
            element_key = self.data.get_element_key(i)  # 获取操作元素
            handle_value = self.data.get_handle_value(i)  # 操作值

            excute_method = getattr(action_method, handle_step)
            # 方法执行 ----> 自动化测试用例集
            if element_key is not None:
                try:
                    excute_method(handle_value)
                except:
                    self.data.write_value(i,"**元素找不到**")


            # #     # 实际结果与预期结果做对比
            # if expect_step is not None:
            #     # 获取预期结果 如果不为空我们就去获取他的预期key
            #     expect_result = getattr(action_method, expect_step)
            #     result = expect_result(expect_key)
            #     if result:
            #         self.data.write_value(i, "pass")
            #     else:
            #         self.data.write_value(i, "fail")






if __name__ == "__main__":
    run = RunMethod()
    run.run_method()
