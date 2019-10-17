# encoding: utf-8

"""
# @Time    : 2019-08-21 10:43
# @Author  : Function
# @FileName    : GetData.py
# @Software: PyCharm

获取数据
"""
from AutoUI.Util.OperaExcel import OpExcel

class Getda:
    def __init__(self,sheetN):
        self.opera_excel = OpExcel(sheetN)
        self.sheetN = sheetN


    def get_case_lines(self):
        """
        获取case的行数 ---> 获取case的行数
        """
        lines = self.opera_excel.get_lines()
        return lines

    def get_caseName(self, row):
        """
        返回 case_Name
        :param row:
        :return:
        """
        case_name = self.opera_excel.get_cell(row, 0)
        if case_name == "":
            return None
        return case_name

    def get_handle_step(self, row):
        """
        对应Excel ---> 步骤
        获取操作步骤里面的操作方法名字(send_key<->OR<->click)
        """
        method_name = self.opera_excel.get_cell(row, 2)
        return method_name

    def get_element_key(self, row):
        """
        对应Excel ---> 元素
        获取元素
        """
        element_key = self.opera_excel.get_cell(row, 3)
        if element_key == '':
            return None
        return element_key

    def get_handle_value(self, row):
        """
        对应Excel ---> 操作值 getByLocal
        获取操作元素的值
        """
        handle_value = self.opera_excel.get_cell(row, 4)
        if handle_value == '':
            return None
        return handle_value

    def get_is_run(self, row):
        """
        是否运行
        :param row:
        :return:
        """
        is_run = self.opera_excel.get_cell(row, 6)
        if is_run == 'yes':
            return True
        else:
            return False

    def get_is_result(self, row):
        """
        获取运行结果 写入运行结果
        :param row:
        :return:
        """
        is_result = self.opera_excel.get_cell(row, 5)
        return is_result



    def write_value(self, row, value,sheetN):
        """
        写入测试结果pass or filed
        :param sheetN:
        :param row:
        :param value:
        :return:
        """
        self.opera_excel.write_value(row, value,sheetN)


if __name__ == '__main__':
    get = Getda(1)
    get.write_value(1,"测试失败")

