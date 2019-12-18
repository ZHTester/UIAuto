import multiprocessing
import threading
from AutoUI.Case.all_main_case import RunMethodAll
from AutoUI.Config.setting import *
from Util.AppiumServer import Serappium
from Util.OtherFunction import pass_flied_statistics

"""
 多线程 启动多个Ui测试端口
"""
class AllThread:
    def __init__(self):
        self.all = RunMethodAll()

    def Run_BB_Android(self):
        """
        娱乐端 Android
        :return:
        """
        self.all.run_method_All(driver_name='android', sheetN=1, Run_name='android',i_num=0, appname=app_name_android_aibet, time_sleep=2)

    def Run_BB_H5(self):
        """
        娱乐端 H5
        :return:
        """
        self.all.run_method_All(driver_name='H5', sheetN=3, Run_name='H5', i_num=1,time_sleep=2)

    def Run_Sport_Android1(self):
        """
        体育对投注 android1
        :return:
        """
        self.all.run_method_All(driver_name='android', sheetN=4, Run_name='android',i_num=1, appname=app_name_android_sport, time_sleep=2)

    def Run_Sport_Android2(self):
        """
        体育对投注 android2
        :return:
        """
        self.all.run_method_All(driver_name='android', sheetN=5, Run_name='android', i_num=0,appname=app_name_android_sport,time_sleep=2)

    def Run_Thread_BB_H5Android(self):
        """
        BB项目 Android H5 多进程
        :return:
        """
        server = Serappium()
        server.main()  # 启动appium服务

        Run_threads = [
            multiprocessing.Process(target=self.Run_BB_Android),
            multiprocessing.Process(target=self.Run_BB_H5)
        ]

        for run_t in Run_threads:
            run_t.start()

    def Run_Thread_Sport_Android(self):
        """
        体育项目 体育对投  多进程
        :return:
        """
        server = Serappium()
        server.main()  # 启动appium服务


        Run_threads = [
            multiprocessing.Process(target=self.Run_Sport_Android1),
            multiprocessing.Process(target=self.Run_Sport_Android2)
        ]

        for run_t in Run_threads:
            run_t.start()

    def run_All(self):
        Run_threads = [
            multiprocessing.Process(target=self.Run_Thread_Sport_Android),
            multiprocessing.Process(target=self.Run_Thread_BB_H5Android)
        ]

        for run_t in Run_threads:
            run_t.start()
            run_t.join()


if __name__ == '__main__':
    c = AllThread()
    c.run_All()





