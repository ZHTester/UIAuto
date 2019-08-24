# encoding: utf-8

"""
# @Time    : 2019-08-21 17:46
# @Author  : Function
# @FileName    : LogData.py
# @Software: PyCharm

log日志
"""
import datetime
import os
import logging


class LogConfig:
    def write_data(self):
        logger = logging.getLogger()
        fh = logging.FileHandler('../Log/log.log')
        sh = logging.StreamHandler()
        logger.addHandler(fh)
        logger.addHandler(sh)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.warning('message')
        logging.log(logging.DEBUG, "This is a debug log.")
        logging.log(logging.INFO, "This is a info log.")
        logging.log(logging.WARNING, "This is a warning log.")
        logging.log(logging.ERROR, "This is a error log.")
        logging.log(logging.CRITICAL, "This is a critical log.")


