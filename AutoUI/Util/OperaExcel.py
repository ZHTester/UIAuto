# encoding: utf-8
"""
# @Time    : 2019-08-20 18:02
# @Author  : Function
# @FileName    : OperaExcel.py
# @Software: PyCharm

相关Case数据存储到Excel中便于数据和Case的相关维护
"""
import time

import xlrd
from xlutils.copy import copy
from AutoUI.Config.setting import *


class OpExcel:
    def __init__(self, Num, file_path=None):
        if file_path is None:
            self.file_path = aibetCase_file
        else:
            self.file_path = file_path
        self.excel = self.get_excel()
        self.data = self.get_sheets(Num)

    def get_excel(self):
        """
        获取excel
        """
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self, i):
        """
        获取sheets的内容
        """
        tables = self.excel.sheets()[i]

        return tables

    def get_lines(self):
        """
        获取excel行数 case总数量
        :return:
        """
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        """
        获取单元格内容
        :param row: 行
        :param cell: 列
        :return:
        """
        data = self.data.cell(row, cell).value
        return data

    def write_value(self, row, value,sheetN):
        """
        写入方法  --- 主要用于写入测试结果 True 或者是 False
        :param sheetN:
        :param row: 行号
        :param value: 写入值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_path,formatting_info=True)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(sheetN)
        sheet_data.write(row, 5, value)
        write_data.save(self.file_path)

if __name__ == '__main__':
    p = OpExcel(0)
    s = p.get_cell(1, 0)  # 获取单元格相关内容
    print("=========----case名称is{0}--------======".format(s))











