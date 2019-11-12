# encoding: utf-8

"""
# @Time    : 2019-09-13 16:27
# @Author  : Function
# @FileName    : Run_all.py
# @Software: PyCharm

总执行case
"""
import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from AutoUI.Case.aibetCase_web import RunMethodWeb
from AutoUI.Case.aibetCase_android import RunMethodAndroid
from AutoUI.Case.aibetCase_ios import RunMethodIos
from AutoUI.Config.setting import *
from AutoUI.Util.ImageZip import make_zip
from Case.aibetCase_H5 import RunMethodH5
from KeyWord.GetData import Getda
from Util.SendEmail import SEmail
from Util.SendHtml import message_send


class RunAll:
    def __init__(self):
        self.ios = RunMethodIos()
        self.android = RunMethodAndroid()
        self.web = RunMethodWeb()
        self.h5 = RunMethodH5()
        self.sendemail = SEmail()

    def Run_main(self):
        pass_count = []
        thread_android = self.android.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1,deviceName='681c4234')
        # thread_web = self.web.run_method_web(driver_name='web',sheetN=2)
        # thread_h5 = self.h5.run_method_H5(driver_name='H5',sheetN=3)
        # thread_ios = self.ios.run_method_ios(driver_name='ios', sheetN=0, appname=app_name_ios_aibet)
        # thread_android = self.android.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1,deviceName='681c4234')


        for sheeti in range(4):
            data = Getda(sheeti)
            caselines = data.get_case_lines()
            for i in range(1, caselines):
                is_run = data.get_is_run(i)
                if is_run is True:
                    result_test = data.get_is_result(i)  # 获取结果
                    print(result_test)
                    # 判断预期元素在当前页面是否存在
                    if result_test != '测试失败':
                        data.write_value(i, "测试通过")
                        pass_count.append(i)

        pass_n = len(pass_count)
        fail_n = pass_n-thread_android
        # fail_n = thread_android + thread_ios + thread_web + thread_h5 - pass_n
        # fail_n = fail_n - pass_n
        print('----------------------------------------',fail_n)
        return pass_n,fail_n

    def send_email(self):
        count = self.Run_main()
        pass_n_1 =count[0]
        fail_n_1 =count[1]
        make_zip(ErrorImage,ErrorImageZip)
        text = message_send(total=count,pass_n=pass_n_1,falied_n=fail_n_1)
        print('---------------消息生成成功----------------------')
        self.sendemail.Email_UiTest(text, aibetCase_file, OUT_FILENAME)
        print('---------------邮件发送成功测试结束---------------')

if __name__ == "__main__":
    r = RunAll()
    r.send_email()










