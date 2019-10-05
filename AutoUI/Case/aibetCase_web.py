# encoding: utf-8

import datetime
import time

from KeyWord.GetData import Getda
from KeyWord.ActionMe_Selenium import ActionMe
from Util.SendEmail import SEmail
from Util.ImageZip import make_zip
from Util.OtherFunction import pass_fail_number
from Config.setting import *


class RunMethodWeb:
    def __getattr__(self, item):
        return "excel 有空格请检查"

    @staticmethod
    def run_method_web(driver_name,sheetN):
        pass_count = []  # 统计成功个数
        fail_count =[]  # 统计失败个数
        data = Getda(sheetN)
        action_method = ActionMe(driver_name,sheetN)
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
                print('-------------------------------', handle_step)
                time.sleep(1)
                excute_method(i,handle_value)
                action_method.ScreenShot(i,handle_value,file_s='../Image/web_img/执行图片/')

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

        # 结果邮件发送
        message = pass_fail_number(pass_count,fail_count)
        sendemail.Email_UiTest(message,aibetCase_file,OUT_FILENAME)


if __name__ == "__main__":
    run = RunMethodWeb()
    run.run_method_web(driver_name='web',sheetN=2)
