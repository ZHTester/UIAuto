# encoding: utf-8

"""
# @Time    : 2019-08-20 14:11
# @Author  : Function
# @FileName    : AppiumServer.py
# @Software: PyCharm

Appium 服务端
"""
import multiprocessing
import time

from AutoUI.Util.Osterminal import OsTerminal
from AutoUI.Util.WriteYaml import WriteYamlCommand
from AutoUI.Util.CheckPort import Cport


class Serappium:
    def __init__(self):
        self.Terminal = OsTerminal()
        self.device_list = self.get_devices()
        self.write_file = WriteYamlCommand()

    @staticmethod
    def get_devices():
        """
        获取设备信息
        :return:
        """
        # devicesli = ['iPhone Xʀ']
        devicesli = ['iPhone Xʀ','192.168.56.102:5555']
        return devicesli

    def create_post_list(self, start_port):
        """
        创建可用端口
        :param start_port:
        :return:
        """
        port = Cport()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        生成命令
        no-reset参数，防止appium删除你的app
        -p是设置appium服务的端口号
        session-override 带上这个参数的话，每次脚本视图启动一个会话的时候都会覆盖上一个会话
        "appium --no-reset -p " + str(appium_port_list[i]) + "--session-override"
        """
        # appium -p 4700 -bp 4701 -U iPhone Xr
        command_list = []
        appium_port_list = self.create_post_list(4700)
        command = "appium -p " + str(appium_port_list[i])
        command_list.append(command)
        self.write_file.write_data(str(appium_port_list[i]))
        return command_list  # 返回生成的命令

    def start_server(self, i):
        """
        启动appium服务器
        :param i: 启动服务的编号
        :return:
        """
        self.start_list = self.create_command_list(i)
        self.Terminal.Excute_terminal(self.start_list[0])

    def kill_server(self):
        """
        杀掉Appium的进程 清空内存
        :return:
        """
        server_list = self.Terminal.Excute_terminal_result('ps aux | grep node')
        if len(server_list) > 0:
            self.Terminal.Excute_terminal('kill -F -PID node')

    def main(self):
        """
        主方法启动appium 通过进程的方式启动
        :return:
        """
        self.write_file.clear_data()
        thread_list = []
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(3)


if __name__ == '__main__':
    s = Serappium()
    s.main()

