# encoding: utf-8

"""
# @Time    : 2019-09-13 16:27
# @Author  : Function
# @FileName    : Run_all.py
# @Software: PyCharm

总执行case
"""
import multiprocessing

from Case.thread_all_case import AllThread
from Util.ImageZip import make_zip
from Util.OtherFunction import pass_flied_statistics
from Util.SendEmail import SEmail
from Util.SendHtml import message_send
from Config.setting import *


class RunAll:
    def __init__(self):
        self.sendemail = SEmail()
        self.sport = AllThread()  # android sport

    def Run_Test(self):
        thread_i = [
            multiprocessing.Process(target=self.sport.Run_Thread_Sport_Android),  # 体育 Android 对投
            multiprocessing.Process(target=self.sport.Run_Thread_BB_H5Android)  # BB项目Android H5
        ]
        for tt in thread_i:
            tt.start()
            tt.join()


    def send_email(self):
        self.Run_Test()
        sport_android_count = pass_flied_statistics(4,6)  # Android 对投返回值
        pass_count = sport_android_count[0]
        file_count = sport_android_count[1]
        totle_count =sport_android_count[2]

        BB_H5_count = pass_flied_statistics(3, 4)  # BB H5 返回值
        pass_count = sport_android_count[0]
        file_count = sport_android_count[1]
        totle_count =sport_android_count[2]
        pass_result =sport_android_count[3]
        fail_result = sport_android_count[4]

        BB_H5_count = pass_flied_statistics(3, 4)  # BB Android 返回值
        pass_count = sport_android_count[0]
        file_count = sport_android_count[1]
        totle_count =sport_android_count[2]
        pass_result =sport_android_count[3]
        fail_result = sport_android_count[4]

        print('====---成功数-{0}---失败数-{1}---总数-{2}'.format(pass_count, file_count, totle_count))

        make_zip(ErrorImage,ErrorImageZip)
        text = message_send(total=totle_count,pass_n=pass_count,falied_n=file_count)
        print('---------------消息生成成功----------------------')
        self.sendemail.Email_UiTest(text, aibetCase_file, OUT_FILENAME)
        print('---------------邮件发送成功测试结束---------------')

if __name__ == "__main__":
    r = RunAll()
    r.send_email()










