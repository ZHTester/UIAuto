# encoding: utf-8

"""
# @Time    : 2019-08-27 14:32
# @Author  : Function
# @FileName    : aibet_setting.py
# @Software: PyCharm
"""
# Other存放路径
report_file = r'../Config/aibet_Case.xls'  # 测试用例存放路径
yam_file = '../Config/aibet.yaml'  # yam 命令生成路径
screen_images_error = r'../aibetImage/ImageError/'  # 错误图片存储路径
images_error = r'../aibetImage/errorImage.zip' # 错误图片zip包路径
screen_images_success = r'../aibetImage/ImageSuccess/' # 成功图片文件路径
images_success = r'../aibetImage/successImage.zip'  # 成功图片文件路径
app_name = 'aibet.app'

# Email相关变量
MAIL_HOST = "secure.emailsrvr.com"  # 设置服务器
MAIL_USER = "Function@seektopser.com"  # 用户名
MAIL_PASS = "function@12345"  # 密码
PORT = "465"  # 发送端口
SENDER = 'Function@seektopser.com'  # 发送者
RECEIVERS = ['Function@seektopser.com']  # 接收邮件
SUBJECT = 'IOS(UI)自动化测试报告' # 邮件主题内容
OUT_FILENAME = 'aibet_Case.xls'


