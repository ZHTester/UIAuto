# encoding: utf-8

"""
# @Time    : 15/11/2019 5:09 下午
# @Author  : Function
# @FileName    : thread_BB_android&&H5.py
# @Software: PyCharm
"""
import multiprocessing

from Case.all_main_case import RunMethodAll
from Config.setting import *
from Util.AppiumServer import Serappium

"""
 android体育 多进程启动 相互对投注
"""
class SportRunAndroid:
    def __init__(self):
        self.all = RunMethodAll()

    def Run_main(self):
        self.all.run_method_All(driver_name='android', sheetN=1, Run_name='android',i_num=0, appname=app_name_android_aibet, time_sleep=2)

    def Run_main01(self):
        self.all.run_method_All(driver_name='H5', sheetN=3, Run_name='H5', i_num=1,time_sleep=2)

    def Run_Thread(self):
        server = Serappium()
        server.main()  # 启动appium服务

        Run_threads = [
            multiprocessing.Process(target=self.Run_main01),
            multiprocessing.Process(target=self.Run_main)
        ]

        for run_t in Run_threads:
            run_t.start()

if __name__ == '__main__':
    c = SportRunAndroid()
    c.Run_Thread()




