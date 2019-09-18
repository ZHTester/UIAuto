# encoding: utf-8

"""
# @Time    : 2019-08-28 15:21
# @Author  : Function
# @FileName    : OtherFunction.py
# @Software: PyCharm

Other方法
"""
import os
import time
import zipfile

from AutoUI.Log.LogData import LogConfig


def pass_fail_number(pass_list,fail_list,end_time):
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
    try:
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        Message = "[IOS(UI)自动化测试执行时间---"+str(end_time)+"]:" \
                                        "\n测试用例个数为%s个" \
                                        "\n*通过个数为%s个*" \
                                        "\n*失败个数为%s个*" \
                                        "\n*通过率为%s*" \
                                        "\n*失败率为%s*" \
                  % (count_num, pass_num, fail_num,
                     pass_result,fail_result ) + "\n*如需了解本次IOS(UI)自动化测试详情,请查看附件!*"
        return Message
    except ZeroDivisionError:
        print('失败数目为0')


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


def deleteFolder(folderPath):
    # 反向查找传入的文件夹路径最后一个字符是否为斜杠
    pos = folderPath.rfind("/")
    if pos > 0:
        # 如果文件夹路径最后一个字符不是斜杠，则在末尾添加斜杠
        folderPath = folderPath + '/'
    try:
        # 获取当前文件夹下文件列表，包括文件和文件夹
        childList = os.listdir(folderPath)
    except Exception as e:
        return e, -1
    # 如果文件夹列表为空，返回异常
    if childList is None:
        print("文件夹不合法")
        return "error", -2

    # 便利当前文件夹下文件名称列表
    for child in childList:
        # 根据判断文件有没有*.*的后缀，区分是文件还是文件夹
        isFile = child.rfind('.')
        if isFile > 0:
            # 如果是文件，对文件进行删除
            os.remove(folderPath + child)
        else:
            # 如果是目录进行递归便利
            deleteFolder(folderPath + child)

    # 递归结束后文件夹已经是空文件夹，直接删除空文件夹
    os.rmdir(folderPath)


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
