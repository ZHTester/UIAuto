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
from aibetPr.Base.BaseDriver import BaDriver
from aibetPr.Util.AppiumServer import Serappium
from aibetPr.Util.GetByLocal import GetByLo
from aibetPr.Log.LogData import LogConfig
from aibetPr.KeyWord.ActionMethod import ActionMe


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
        self.getbylo.get_element.click()
        print('''''执行完成这是第一步''')
        time.sleep(10)
        print('''''这是第二步''')
        self.getbylo.get_element.click()
        print('''''执行完成这是第二步''')
        pass


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()