# encoding: utf-8

"""
# @Time    : 2019-08-20 10:12
# @Author  : Function
# @FileName    : CheckPort.py
# @Software: PyCharm

检查端口是否可用启动appium需要
生成端口 - 检测端口是否可用  'lsof -i :' + port_num
生成端口 - 生成我们可用的端口
lsof -i
"""
from AutioIOS.Util.Osterminal import OsTerminal
import os


class Cport:
    def __init__(self):
        self.Ter = OsTerminal()

    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num: 传入端口
        :return: 被占用返回False 未被占用返回True
        """
        command = 'lsof -i :' + str(port_num)
        result = self.Ter.Excute_terminal_result(command)
        # 判断是否含有有结果返回是否被占用 占用返回True 未被占用返回False
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        生成可用端口
        @parameter start_port 开始端口
        @parameter device_list 开始多少个服务就生成多个端口数
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) is not True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print("生成可用端口失败")
            return None


if __name__ == "__main__":
    f = Cport()
    print(f.port_is_used('4748'))  # 判断端口是否被占用
    # print(os.system('lsof -i :4711'))
    li = [1, 2, 4, 5, 7, 8, 9]  # 需要生成的端口数量
    print(f.create_port_list(4747, li))
