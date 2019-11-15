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

    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        devices_list = []
        result_list = self.Terminal.Excute_terminal_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t') or i.split('\n')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
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
        android - 生成命令
        """
        # appium -p 4700 -bp 4701 -U iPhone Xr
        command_list = []
        appium_port_list = self.create_port_list(4720)
        bootstrap_port_list = self.create_port_list(4920)
        systemPort = self.create_port_list(8210)
        device_list = self.device_list
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  device_list[i] + " --log ../log/Appium_Log.txt "
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]),systemPort)
        print(command_list)
        return command_list

    def start_server(self, i):
        """
        :param i:
        :return:
        """
        self.start_list = self.create_command_list(i)
        self.Terminal.Excute_terminal(self.start_list[0])

    def kill_server(self):
        """
        杀掉Appium的进程 清空内存  mac环境
        :return:
        """
        server_list = self.Terminal.Excute_terminal_result('ps -ef | grep node')
        if len(server_list) > 0:
            self.Terminal.Excute_terminal("ps -ef | grep node | awk '{print $2}' | xargs kill -9")

    def main(self):
        """
        主方法启动appium 通过进程的方式启动
        :return:
        """
        self.write_file.clear_data()
        self.kill_server()
        thread_list = []
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(3)


if __name__ == '__main__':
    s = Serappium()
    print(s.create_command_list(0))

