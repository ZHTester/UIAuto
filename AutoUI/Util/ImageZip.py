# encoding: utf-8

"""
# @Time    : 2019-08-28 09:47
# @Author  : Function
# @FileName    : ImageZip.py
# @Software: PyCharm

压缩图片脚本 压缩错误
"""
import os
import zipfile
import os
import mimetypes
from email.mime.base import MIMEBase
from email import encoders


def make_zip(source_dir, output_filename):
    """
    压缩文件夹
    :param source_dir:  目标文件
    :param output_filename:  输出文件
    :return:
    """
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep) #相对路径
            zipf.write(pathfile, arcname)
    print('---------------压缩成功-------------')


def annex(zipName):
    """
    图片文件压缩邮件发送
    :param zipName:
    :return:
    """
    try:
        data = open(zipName,'rb')
        ctype,encoding = mimetypes.guess_type(zipName)
        if ctype is None or encoding is not None:
            ctype = 'application/x-zip-compressed'
        maintype,subtype = ctype.split('/',1)
        file_msg = MIMEBase(maintype,subtype)
        file_msg.set_payload(data.read())
        data.close()
        encoders.encode_base64(file_msg)
        basename = os.path.basename(zipName)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
        return file_msg
    except:
        print('添加文件附件失败')
        raise

if __name__ == '__main__':
    make_zip(screen_images_error, r'../ziii.zip')