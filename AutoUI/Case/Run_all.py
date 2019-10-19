# encoding: utf-8

"""
# @Time    : 2019-09-13 16:27
# @Author  : Function
# @FileName    : Run_all.py
# @Software: PyCharm

总执行case
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from AutoUI.Case.aibetCase_web import RunMethodWeb
from AutoUI.Case.aibetCase_android import RunMethodAndroid
from AutoUI.Case.aibetCase_ios import RunMethodIos
from AutoUI.Config.setting import *
from AutoUI.Util.ImageZip import make_zip
from AutoUI.Util.OtherFunction import pass_fail_number
from KeyWord.GetData import Getda
from Util.SendEmail import SEmail


class RunAll:
    def __init__(self):
        self.ios = RunMethodIos()
        self.android = RunMethodAndroid()
        self.web = RunMethodWeb()
        self.sendemail = SEmail()

    def Run_main(self):
        pass_count = []
        thread_android = self.android.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1,deviceName='681c4234')
        thread_ios = self.ios.run_method_ios(driver_name='ios', sheetN=0, appname=app_name_ios_aibet)
        thread_web = self.web.run_method_web(driver_name='web',sheetN=2)

        # excutor = ThreadPoolExecutor(max_workers=2)
        # task1 = excutor.submit(self.ios.run_method_ios(driver_name='ios', sheetN=0, appname= app_name_ios_aibet))  # 向线程池中添加函数
        # task2 = excutor.submit(self.android.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1,deviceName='681c4234'))  # 向线程池中添加函数

        for sheeti in range(3):
            data = Getda(sheeti)
            caselines = data.get_case_lines()
            for i in range(1, caselines):
                is_run = data.get_is_run(i)
                if is_run is True:
                    result_test = data.get_is_result(i)  # 获取结果
                    # 判断预期元素在当前页面是否存在
                    if result_test != '测试失败':
                        data.write_value(i, "测试通过")
                        pass_count.append(i)

        pass_n = len(pass_count)
        fail_n = thread_android+thread_ios+thread_web - pass_n
        print('----------------------------------------',fail_n)
        return pass_n,fail_n

    def send_email(self):
        count = self.Run_main()
        pass_n =count[0]
        fail_n =count[1]
        make_zip(ErrorImage,ErrorImageZip)
        message = pass_fail_number(pass_n,fail_n)
        print('---------------消息生成成功----------------------')
        self.sendemail.Email_UiTest(message, aibetCase_file, OUT_FILENAME)
        print('---------------邮件发送成功测试结束---------------')

if __name__ == "__main__":
    r = RunAll()
    r.send_email()










