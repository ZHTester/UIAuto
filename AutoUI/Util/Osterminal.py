# encoding: utf-8

"""
# @Time    : 2019-08-20 09:49
# @Author  : Function
# @FileName    : Osterminal.py
# @Software: PyCharm

通过 OStesrminal来启动appium服务端
"""
import os


class OsTerminal:
    def Excute_terminal_result(self, command):
        """
        启动多个服务端结果集方法
        :param command: os 命令
        :return: 返回结果集
        """
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':  # 遇到空格继续取值跳过空格
                continue
            result_list.append(i.strip('\n'))  # 以空格分割取出值
        return result_list

    def Excute_terminal(self, command):
        """
        单一结果集
        :param command: os命令
        :return:
        """
        os.system(command)


if __name__ == "__main__":
    ter = OsTerminal()
    val = os.system('top')
    # print(ter.Excute_terminal_result(val))  # 启动服务端服务


