# encoding: utf-8

"""
# @Time    : 2019-09-13 16:27
# @Author  : Function
# @FileName    : Run_all.py
# @Software: PyCharm

总执行case
"""

from Case.thread_case.thread_sport_aa import SportRunAndroid
from Util.OtherFunction import pass_flied_statistics
from Util.SendEmail import SEmail
from Util.SendHtml import message_send


class RunAll:
    def __init__(self):
        self.sendemail = SEmail()
        self.sport = SportRunAndroid()  # android sport

    def Run_Test(self):
        self.sport.Run_Thread()


    def send_email(self):
        self.Run_Test()
        count = pass_flied_statistics(4,6)
        print(count)

        # pass_n_1 =count[0]
        # fail_n_1 =count[1]
        # make_zip(ErrorImage,ErrorImageZip)
        # text = message_send(total=count,pass_n=pass_n_1,falied_n=fail_n_1)
        # print('---------------消息生成成功----------------------')
        # self.sendemail.Email_UiTest(text, aibetCase_file, OUT_FILENAME)
        # print('---------------邮件发送成功测试结束---------------')

if __name__ == "__main__":
    r = RunAll()
    r.send_email()










