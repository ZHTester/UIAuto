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

from AutoUI.Case.aibetCase_web import RunMethodWeb
from AutoUI.Case.aibetCase_android import RunMethodAndroid
from AutoUI.Case.aibetCase_ios import RunMethodIos
from AutoUI.Config.setting import *
from AutoUI.Util.ImageZip import make_zip
from AutoUI.Util.OtherFunction import pass_fail_number
from Util.SendEmail import SEmail


class RunAll:
    def __init__(self):
        self.ios = RunMethodIos()
        self.android = RunMethodAndroid()
        self.web = RunMethodWeb()
        self.sendemail = SEmail()

    def Run_main(self):
        thread_android = self.android.run_method_adnroid(driver_name='android',sheetN=1,appname = app_name_android_aibet)
        thread_ios = self.ios.run_method_ios(driver_name='ios', sheetN=0, appname= app_name_ios_aibet)
        # thread_web = threading.Thread(target=self.web.run_method_web(driver_name='web',sheetN=2))

        pass_n = int(thread_android[0]+thread_ios[0])
        fail_n = int(thread_android[1]+thread_ios[1])

        return pass_n,fail_n

    def send_email(self):
        count = self.Run_main()
        pass_n =count[0]
        fail_n =count[1]
        make_zip(ErrorImage,ErrorImageZip)
        message = pass_fail_number(pass_n,fail_n)
        print('---------------消息生成成功---------------')
        self.sendemail.Email_UiTest(message, aibetCase_file, OUT_FILENAME)
        print('---------------邮件发送成功测试结束---------------')

if __name__ == "__main__":
    r = RunAll()
    r.send_email()










