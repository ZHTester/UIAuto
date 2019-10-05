# encoding: utf-8

"""
# @Time    : 2019-09-27 10:40
# @Author  : Function
# @FileName    : LoginBackendXJ.py
# @Software: PyCharm
"""
import requests, time, threading


class Presstest(object):
    def __init__(self, XJurl):
        self.XJurl = XJurl

    def testinterface(self,key,value):
        """压测接口"""
        data1 = {
                "username":key,
                "password":value
                }
        global ERROR_NUM
        try:
            res = requests.post(url=self.XJurl, data=data1)
            print(res.json())
            if res.json()['code'] is not 1:
                print(key)
                ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self,key,value):
        """一次并发处理单个任务"""
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.testinterface(key,value)

        time.sleep(LOOP_SLEEP)

    def run(self):
        """使用多线程进程并发测试"""
        t1 = time.time()
        Threads = []
        list_data = {'elma001':'1234qwer',"elma002":"1234qwer","elma003":"1234qwer","elma004":"1234qwer","elma005":"1234qwer",
                     "elma006":"1234qwer","elma007":"1234qwer","rita27":"q12345678","rita37":"q12345678","rita47":"q12345678",
                     "rita57":"q12345678","rita67":"q12345678","rita17":"q12345678","rita87":"q12345678","rita99":"q12345678",
                     "fly111":"akl123456","fly222":"akl123456","hytest0":"a123456654321","hytest2":"a123456654321",
                     "frank12345":"frank123"
                     }
        for i in range(THREAD_NUM):
         for k, v in list_data.items():
                t = threading.Thread(target=self.testonework, args=(k,v))
                t.setDaemon(True)
                Threads.append(t)
        for t in Threads:
            t.start()
        for t in Threads:
            t.join()
        t2 = time.time()

        print("===============压测结果===================")
        print("URL:", self.XJurl)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)

if __name__ == '__main__':
    XJurl = 'http://www.sport-server.top/sportApi/loginBackendAndXJ'
    THREAD_NUM = 1 # 并发线程总数
    ONE_WORKER_NUM = 1  # 每个线程的循环次数
    LOOP_SLEEP = 0.00000000001 # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = Presstest(XJurl=XJurl)
    obj.run()
