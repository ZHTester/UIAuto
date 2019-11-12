import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from AutoUI.Case.aibetCase_web import RunMethodWeb
from AutoUI.Case.aibetCase_android import RunMethodAndroid
from AutoUI.Case.aibetCase_ios import RunMethodIos
from AutoUI.Config.setting import *
from Case.aibetCase_H5 import RunMethodH5
from Util.SendEmail import SEmail


class RunAll:
    def __init__(self):
        self.ios = RunMethodIos()
        self.android = RunMethodAndroid()
        self.web = RunMethodWeb()
        self.h5 = RunMethodH5()
        self.sendemail = SEmail()

    def Run_main(self):
        self.android.run_method_adnroid(driver_name='android', appname=app_name_android_aibet, sheetN=1)

    def Run_main01(self):
        self.h5.run_method_H5(driver_name='H5',sheetN=3)




if __name__ == '__main__':
    c = RunAll()
    threads = [threading.Thread(target=c.Run_main),
               threading.Thread(target=c.Run_main01)]
    for t in threads:
        # 启动线程
        t.start()
