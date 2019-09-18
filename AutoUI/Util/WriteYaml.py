# encoding: utf-8

"""
# @Time    : 2019-08-20 13:41
# @Author  : Function
# @FileName    : WriteYaml.py
# @Software: PyCharm

操作Yaml文件 存储appium启动命令
"""
import yaml
from AutoUI.Config.aibet_setting import yam_file


class WriteYamlCommand:
    def read_data(self):
        """
        加载yaml数据
        """
        with open(yam_file) as fr:
            data = yaml.load(fr, Loader=yaml.FullLoader)
        return data

    def get_value(self, key):
        """
        获取value
        """
        data = self.read_data()
        value = data[key]
        return value

    def write_data(self, port):
        """
        写入数据
        """
        data = self.join_data(port)
        with open("../Config/aibet.yaml", "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, port):
        """
        拼接启动命令
        :param port: 端口号
        :return: 返回拼接命令行
        """
        data = {
            "port": port
        }
        return data

    def clear_data(self):
        """
        清空Yaml文件清除内存(为kill appium做好准备)
        :return:
        """
        with open("../Config/aibet.yaml", "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        """
        获取Yaml文件中的行数 给appium Server启动端启动appium服务
        :return:
        """
        data = self.read_data()
        return len(data)


if __name__ == "__main__":
    w = WriteYamlCommand()
    c = w.get_value('port')
    print(c)









