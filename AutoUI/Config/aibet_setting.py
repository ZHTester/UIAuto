# encoding: utf-8

"""
# @Time    : 2019-08-27 14:32
# @Author  : Function
# @FileName    : aibet_setting.py
# @Software: PyCharm
"""
# Other存放路径
aibetCase_Ios_file = r'../Config/aibetCase_Ios.xls'  # 测试用例存放路径
aibetCase_Android_file = r'../Config/aibetCase_Android.xls'  # 测试用例存放路径
yam_file = r'../Config/aibet.yaml'  # yam 命令生成路径
screen_images_error = r'../Image/IOS_aibetImageI/ImageError/'  # 错误图片存储路径
images_error = r'../Image/IOS_aibetImageI/errorImage.zip' # 错误图片zip包路径
screen_images_success = r'../Image/IOS_aibetImageI/ImageSuccess/' # 成功图片文件路径
images_success = r'../Image/IOS_aibetImageI/successImage.zip'  # 成功图片文件路径
lun_image = r'../Image/IOS_aibetImageI/lunImage/'
app_name_ios_aibet = 'aibet.app'
app_name_android_aibet = 'ballbet.apk'

# Email相关变量
MAIL_HOST = "secure.emailsrvr.com"  # 设置服务器
MAIL_USER = "Function@seektopser.com"  # 用户名
MAIL_PASS = "function@12345"  # 密码
PORT = "465"  # 发送端口
SENDER = 'Function@seektopser.com'  # 发送者
RECEIVERS = ['Function@seektopser.com','elma@seektopser.com']  # 接收邮件
SUBJECT = 'IOS(UI)自动化测试报告' # 邮件主题内容
OUT_FILENAME = 'aibetCase_Ios.xls'


