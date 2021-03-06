# encoding: utf-8

"""
# @Time    : 2019-08-28 15:21
# @Author  : Function
# @FileName    : OtherFunction.py
# @Software: PyCharm

Other方法
"""
import os
import zipfile
from xlutils.copy import copy
import xlrd
from AutoUI.Util.OperaExcel import OpExcel
from KeyWord.GetData import Getda


def pass_fail_number(pass_list,fail_list):
    """
    发送消息
    :return:
    """
    pass_num = float(pass_list)  # 百分比就是float 也就是浮点类型
    fail_num = float(fail_list)
    count_num = pass_num + fail_num  # 测试用例总数
    # 90%
    pass_result = "%.2f%%" % (pass_num / count_num * 100)
    fail_result = "%.2f%%" % (fail_num / count_num * 100)


    content = ["[**********UI自动化测试**********]:",
               "本次UI自动化测试共执行测试用例个数为:%s" % count_num,
               "*1*通过个数为:%s个" % pass_num,
               "*2*失败个数为:%s个" % fail_num,
               "*3*通过率为:%s" % pass_result,
               "*4*失败率为:%s"%fail_result
               ]

    msg = '\n'.join(content)
    return  msg


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

def creatFile(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return path
    else:
        return path


def pass_flied_statistics(start_num,end_num):
        """
        失败数  成功数 总数统计
        :return:
        """
        pass_count = []
        totle_count = []
        for sheeti in range(start_num,end_num):
            data = Getda(sheeti)
            caselines = data.get_case_lines()
            for i in range(1, caselines):
                is_run = data.get_is_run(i)
                if is_run is True:
                    totle_count.append(i)
                    result_test = data.get_is_result(i)  # 获取结果 ----
                    # 判断预期元素在当前页面是否存在
                    if result_test != '测试失败':
                        data.write_value(i, "测试通过")
                        pass_count.append(i)

        pass_count = len(pass_count)
        totle_count = len(totle_count)
        file_count = totle_count - pass_count
        pass_result = "%.2f%%" % (pass_count / totle_count * 100)
        fail_result = "%.2f%%" % (file_count / totle_count * 100)

        print('====---成功数-{0}---失败数-{1}---总数-{2}'.format(pass_count,file_count,totle_count))
        return pass_count,file_count,totle_count,pass_result,fail_result
def  wr():
    data  = OpExcel(0,file_path=r'../Config/test.xls')
    read_data = xlrd.open_workbook(r'../Config/test.xls')
    write_data = copy(read_data)
    sheet_data = write_data.get_sheet(0)
    for i in range(16):
        te = data.get_cell(i, 0)
        print(te)
        print(type(te))
        if te != "测试失败":
            sheet_data.write(i, 0, "测试通过")
            write_data.save(r'../Config/test.xls')
            write_data.close()
            print("写入成功")

if __name__ == "__main__":
    wr()

