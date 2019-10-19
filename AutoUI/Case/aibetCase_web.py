# encoding: utf-8

import datetime
import time

from KeyWord.GetData import Getda
from KeyWord.ActionMe_Selenium import ActionMe


class RunMethodWeb:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_web(driver_name,sheetN):
        total_count = []  # 总数
        data = Getda(sheetN)
        action_method = ActionMe(driver_name, sheetN)
        caselines = data.get_case_lines()
        start = datetime.datetime.now()
        print("------------start time  used---------------:", start)

        for i in range(1, caselines):
            is_run = data.get_is_run(i)
            if is_run is True:
                handle_step = data.get_handle_step(i)  # 执行方法
                handle_value = data.get_handle_value(i)  # 操作值

                # 自动化测试用例集执行
                excute_method = getattr(action_method, handle_step)
                print('-------------------------执行到行数-------------------------', i)
                time.sleep(2)
                excute_method(i, handle_value)
                action_method.ScreenShot(i, handle_value, file_s='../Image/android_img/执行图片/')
                total_count.append(i)
        end = datetime.datetime.now()
        print("------------Time used---------------:", end - start)

        total = len(total_count)
        return total

if __name__ == "__main__":
    run = RunMethodWeb()
    r  = run.run_method_web(driver_name='web',sheetN=2)

