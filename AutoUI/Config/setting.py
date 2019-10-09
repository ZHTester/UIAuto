# encoding: utf-8

"""
# @Time    : 2019-08-27 14:32
# @Author  : Function
# @FileName    : setting.py
# @Software: PyCharm
"""
# Other存放路径
aibetCase_file = r'../Config/AutoCase.xls'  # 测试用例存放路径
yam_file = r'../Config/AppiumPort.yaml'  # yam 命令生成路径
screen_images_error = r'../Image/IOS_aibet_Image/ImageError/'  # 错误图片存储路径
images_error = r'../Image/IOS_aibet_Image/errorImage.zip' # 错误图片zip包路径
screen_images_success = r'../Image/IOS_aibet_Image/ImageSuccess/' # 成功图片文件路径
images_success = r'../Image/IOS_aibet_Image/successImage.zip'  # 成功图片文件路径
lun_image = r'../Image/IOS_aibet_Image/lunImage/'
LunImage = r'../Image/IOS_aibet_Image/lunImage.zip'
app_name_ios_aibet = "aibet.app"
app_name_android_aibet = "ballbet.apk"

# Email相关变量
MAIL_HOST = "secure.emailsrvr.com"  # 设置服务器
MAIL_USER = "Function@seektopser.com"  # 用户名
MAIL_PASS = "function@12345"  # 密码
PORT = "465"  # 发送端口
SENDER = 'Function@seektopser.com'  # 发送者
RECEIVERS = ['Function@seektopser.com','felix@seektopser.com']  # 接收邮件
SUBJECT = 'IOS(UI)自动化测试报告' # 邮件主题内容
OUT_FILENAME = 'AutoCase.xls'


