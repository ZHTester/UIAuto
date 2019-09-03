# encoding: utf-8

"""
# @Time    : 2019-08-28 15:21
# @Author  : Function
# @FileName    : OtherFunction.py
# @Software: PyCharm

Other方法
"""
import time
import zipfile

from AutoIOS.Log.LogData import LogConfig


def pass_fail_number(pass_list,fail_list,app_name):
    """
    Email 发送消息
    :param pass_list:
    :param fail_list:
    :param app_name:
    :return:
    """
    pass_num = float(len(pass_list))  # 浮点类型
    fail_num = float(len(fail_list))
    count_num = pass_num + fail_num  # 用例总数

    pass_result = "%.2f%%" % (pass_num / count_num * 100)
    fail_result = "%.2f%%" % (fail_num / count_num * 100)
    now = time.strftime("%Y-%m-%d&&%H:%M:%S", time.localtime())

    Message = "[--"+app_name+"--IOS(UI)自动化测试]:" \
                                    "\n测试用例个数为%s个" \
                                    "\n*通过个数为%s个*" \
                                    "\n*失败个数为%s个*" \
                                    "\n*通过率为%s*" \
                                    "\n*失败率为%s*" \
              % (count_num, "\n\033[0;92m{num}\033[0m".format(num=pass_num), "\033[0;31m{num}\033[0m".format(num=fail_num),
                 "\033[0;92m{num}\033[0m".format(num=pass_result),"\033[0;31m{result}\033[0m".format(result=fail_result) ) + "" \
                                                                            "\n*如需了解本次IOS(UI)自动化测试详情,请查看附件!*"

    return Message

def Zip_size(filename):
    """
    判断压缩文件大小
    :return:
    """
    z = zipfile.ZipFile(filename, "r")
    zz = []
    for filename in z.namelist():
        byte_size = z.read(filename)
        si = len(byte_size)
        zz.append(si)
    return len(zz)

def LogReport():
    log = LogConfig('all.log', level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    LogConfig('error.log', level='error').logger.error('error')

if __name__ == "__main__":
    print("\033[0;92m%s\033[0m" % "输出红色字符")
