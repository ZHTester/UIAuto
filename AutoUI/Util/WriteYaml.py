# encoding: utf-8

"""
# @Time    : 2019-08-20 13:41
# @Author  : Function
# @FileName    : WriteYaml.py
# @Software: PyCharm

操作Yaml文件 存储appium启动命令
"""
import yaml
from AutoUI.Config.setting import yam_file


class WriteYamlCommand:
    @staticmethod
    def read_data():
        """
        加载yaml数据
        """
        with open(yam_file) as fr:
            data = yaml.load(fr, Loader=yaml.FullLoader)
        return data

    def get_value(self, key, port):
        '''
        获取value
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self,i,device,bp,port,systemPort):
        """
        写入数据
        """
        data = self.join_data(i,device,bp,port,systemPort)
        with open("../Config/AppiumPort.yaml", "a") as fr:
            yaml.dump(data, fr)

    def join_data(self,i,device,bp,port,systemPort):
        """
        拼接启动命令
        :param port: 端口号
        :return: 返回拼接命令行
        """
        data = {
            "user_info_" + str(i): {
            "deviceName": device,
            "bp": bp,
            "port": port,
            "systemPort":systemPort
            }
        }
        return data

    def clear_data(self):
        """
        清空Yaml文件清除内存(为kill appium做好准备)
        :return:
        """
        with open("../Config/AppiumPort.yaml", "w") as fr:
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
    a = w.get_file_lines()
    print(a)









