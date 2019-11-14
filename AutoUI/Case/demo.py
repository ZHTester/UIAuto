import multiprocessing
import threading
import time

from AutoUI.Case.demo0001 import RunMethodAll
from AutoUI.Config.setting import *
from Util.AppiumServer import Serappium


class RunAll:
    def __init__(self):
        self.all = RunMethodAll()

    def Run_main(self):
        self.all.run_method_All(driver_name='android', sheetN=4, Run_name='android',i_num=1, appname=app_name_android_sport, time_sleep=2)
        # self.all.run_method_All(driver_name='android',  sheetN=1, Run_name='android',appname="ballbet.apk",time_sleep=2)
        # self.all.run_method_All(driver_name='H5', sheetN=3, Run_name='H5',time_sleep=2)

    def Run_main01(self):
        # self.all.run_method_All(driver_name='web',sheetN=2,Run_name='web',time_sleep=2)
        self.all.run_method_All(driver_name='android', sheetN=5, Run_name='android', i_num=0,appname=app_name_android_sport,time_sleep=2)


if __name__ == '__main__':
    server = Serappium()
    server.main()  # 启动appium服务
    c = RunAll()


    threads = [
        multiprocessing.Process(target=c.Run_main01),
        multiprocessing.Process(target=c.Run_main),
        # threading.Thread(target=c.Run_main01),
        # threading.Thread(target=c.Run_main)
               ]
    for t in threads:
        # 启动线程
        t.start()

