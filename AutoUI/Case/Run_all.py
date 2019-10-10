# encoding: utf-8

"""
# @Time    : 2019-09-13 16:27
# @Author  : Function
# @FileName    : Run_all.py
# @Software: PyCharm

总执行case
"""
import threading
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
        thread_android = threading.Thread(target=self.android.run_method_adnroid(driver_name='android',sheetN=1,appname = app_name_android_aibet))
        thread_ios = threading.Thread(target=self.ios.run_method_ios(driver_name='ios', sheetN=0, appname= app_name_ios_aibet))
        thread_web = threading.Thread(target=self.web.run.run_method_web(driver_name='web',sheetN=2))

        threads = [thread_android,thread_ios,thread_web]

        for j in threads:
            j.start()
        total = self.ios + self.android + self.web
        return total

    def send_email(self):
        total = self.Run_main()
        make_zip(ErrorImage,ErrorImageZip)
        message = pass_fail_number(total)
        self.sendemail.Email_UiTest(message, aibetCase_file, OUT_FILENAME)



if __name__ == "__main__":
    r = RunAll()
    r.send_email()










