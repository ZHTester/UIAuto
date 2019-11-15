import multiprocessing

from AutoUI.Case.all_main_case import RunMethodAll
from AutoUI.Config.setting import *
from Util.AppiumServer import Serappium

"""
 android 多进程启动 相互对投注
"""
class SportRunAndroid:
    def __init__(self):
        self.all = RunMethodAll()

    def Run_main(self):
        self.all.run_method_All(driver_name='android', sheetN=4, Run_name='android',i_num=1, appname=app_name_android_sport, time_sleep=2)
        # self.all.run_method_All(driver_name='android',  sheetN=1, Run_name='android',appname="ballbet.apk",time_sleep=2)
        # self.all.run_method_All(driver_name='H5', sheetN=3, Run_name='H5',time_sleep=2)

    def Run_main01(self):
        # self.all.run_method_All(driver_name='web',sheetN=2,Run_name='web',time_sleep=2)
        self.all.run_method_All(driver_name='android', sheetN=5, Run_name='android', i_num=0,appname=app_name_android_sport,time_sleep=2)

    def Run_Thread(self):

        Run_threads = [
            multiprocessing.Process(target=self.Run_main01),
            multiprocessing.Process(target=self.Run_main)
        ]

        for run_t in Run_threads:
            run_t.start()



if __name__ == '__main__':
    server = Serappium()
    server.main()  # 启动appium服务
    c = SportRunAndroid()
    c.Run_Thread()


