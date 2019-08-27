# encoding: utf-8

"""
# @Time    : 2019-08-20 09:42
# @Author  : Function
# @FileName    : CaseTest.py
# @Software: PyCharm
测试脚本

"""
import unittest
import time
from AutioIOS.Base.BaseDriver import BaDriver
from AutioIOS.Util.AppiumServer import Serappium
from AutioIOS.Util.GetByLocal import GetByLo
from AutioIOS.Log.LogData import LogConfig
from AutioIOS.KeyWord.ActionMethod import ActionMe


class Ioscase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.badriver = BaDriver()
        self.Server = Serappium()
        self.log = LogConfig()
        self.Server.main()
        self.methodac = ActionMe()
        self.driver = self.badriver.get_ios_driver()
        self.getbylo = GetByLo(self.driver)


    def test_Demo01(self):
        self.log.write_data()
        time.sleep(5)
        print('''''这是第一步''')
        self.getbylo.get_element(1).click()
        print('''''执行完成这是第一步''')
        time.sleep(10)
        print('''''这是第二步''')
        self.getbylo.get_element(2).click()
        print('''''执行完成这是第二步''')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
