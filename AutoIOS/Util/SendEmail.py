# encoding: utf-8

"""
# @Time    : 2019-08-20 18:51
# @Author  : Function
# @FileName    : SendEmail.py
# @Software: PyCharm

发送 SendEmail
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from AutoIOS.Config.aibet_setting import *


class SEmail:
    def Email_UiTest(self, send_message):
        # 相关变量读取配置文件
        mail_host= MAIL_HOST
        mail_user= MAIL_USER
        mail_pass= MAIL_PASS
        port = PORT
        sender = SENDER
        receivers = RECEIVERS

        # 定义邮件格式
        message = MIMEMultipart()
        message['From'] = Header(sender)
        message['To'] = Header(','.join(receivers))
        subject = SUBJECT
        message['Subject'] = Header(subject, 'utf-8')

        # 构造邮件主题内容
        text = send_message
        body = MIMEText(text, _subtype="html", _charset="utf-8")
        message.attach(body)

        att1 = MIMEText(open(report_file, 'rb').read(), 'base32', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(report_file)))
        att1["Content-Disposition"] = 'attachment; filename="aibetUIAuto.xls"'
        message.attach(att1)

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,port)
            print ("邮件发送成功")
        except smtplib.SMTPException:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()

if __name__ == '__main__':
    send = SEmail()
    send.Email_UiTest("娱乐端app(ios)自动化测试报告\n以下就是ui自动化测试报告")