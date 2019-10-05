# encoding: utf-8

"""
# @Time    : 2019-09-27 15:01
# @Author  : Function
# @FileName    : getMatchDetail.py
# @Software: PyCharm
获取赛事列表 性能测试脚本

"""
import requests, time, threading,json


class Presstest(object):
    def __init__(self, XJ_Url,XJMatch_Url):
        self.XJurl = XJ_Url
        self.XJMatchUrl = XJMatch_Url

    def get_Uid(self,key,value):
        """获取UID的"""
        data1 = {
                "username":key,
                "password":value
                }
        try:
            res = requests.post(url=self.XJurl, data=data1).json()
            headers_uid = str(res['data']['uid'])
            return headers_uid
        except KeyError:
            print('登陆失败')

    def testinterface(self,key,value):
        """压测接口"""
        data4 = {
            "dataType": -2,
            "inPlay": True,
            "oddType": 1,
            "pageNumber": 0,
            "pageType": 4,
            "sortBy": 1,
            "sportId": [1]
        }
        headers4 = {'uid': self.get_Uid(key,value), "Content-Type": "application/json"}
        global ERROR_NUM
        try:
            res = requests.post(url=self.XJMatchUrl, data=json.dumps(data4), headers =headers4)
            print(res.json())
            if res.json()['code'] is not 1:
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
        """
        并发启动
        """
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
    XJurl = 'http://www.sport-server.top/sportApi/loginBackendAndXJ' # 登陆小金地址
    XJMatchUrl = 'http://www.sport-server.top/sportApi/getMatch'
    THREAD_NUM = 1 # 并发线程总数
    ONE_WORKER_NUM = 10  # 每个线程的循环次数
    LOOP_SLEEP = 1 # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = Presstest(XJ_Url=XJurl,XJMatch_Url=XJMatchUrl)
    obj.run()

