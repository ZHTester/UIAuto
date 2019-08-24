# encoding: utf-8

"""
# @Time    : 2019-08-20 18:51
# @Author  : Function
# @FileName    : SendEmail.py
# @Software: PyCharm

发送 SendEmail
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SEmail:
    def Email_UiTest(self):
        mail_host="smtp.gmail.com"  #设置服务器
        mail_user="Function@seektopser.com"    #用户名
        mail_pass="function@123"   # 密码
        port = "465"

        sender = 'Function@seektopser.com'
        receivers = ['15928737095@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
        message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
        message['To'] = Header("15928737095@163.com", 'utf-8')  # 接收者

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,port)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()
            print ("邮件发送成功")
        except smtplib.SMTPException:
            print('"Error: 无法发送邮件"')

if __name__ == '__main__':
    send = SEmail()
    send.Email_UiTest()