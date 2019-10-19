# # # # encoding: utf-8
# # #
# # # """
# # # # @Time    : 2019-09-25 18:53
# # # # @Author  : Function
# # # # @FileName    : demo.py
# # # # @Software: PyCharm
# # # """
# import time
# import json
# import requests
# from hashlib import md5
#
#
#
# url1 = "http://mutest.ballbet5.com/api/gl/login/username"
# list_body = {"username":"auto123",
#              "password":'auto123123',
#              "productType":1
#              }
# dic_header = {'device-id': '1594290655',
#                 'os-type': '0'
#               }
#
# def encrypt_md5(s):
#     # 创建md5对象
#     new_md5 = md5()
#     new_md5.update(s.encode(encoding='utf-8'))
#     # 加密
#     return new_md5.hexdigest()
#
# def getToken():
#     str_time = (str(time.time())[0:10]) + "000"
#     dic_header.update({'timestamp': str_time, 'version': '1.0'})
#
#     # 拼接字符串
#     list = []
#     for key in dic_header:
#         list.append(key)
#         list.append('=')
#         list.append(dic_header[key])
#         list.append('&')
#     linkString = ''.join(list)[0:-1]
#
#     # 生成签名
#     secret = "global"
#     str_sign = linkString + secret
#     sign = encrypt_md5(str_sign)
#     dic_sign = {"sign": sign}
#
#     dic_header.update(dic_sign)
#     return dic_header
#
#  # 获取token
# dic_header1 = getToken()
# res1 = requests.post(url=url1, data=list_body, headers=dic_header1).json()
# token = res1['data']['token']
# dic_header.update({'token': token})
# print(res1)
#
#
# # #
# # # uid = '428067'
# # # dic_uid = {"uid": uid}
# # # dic_header.update(dic_uid)
# # #
# # #
# # # url2 = 'http://mutest.ballbet5.com/api/game/jump'
# # # data2 = {"gameId":14,"type":0,"productType":1}
# # #
# # # res = requests.post(url=url2,data=data2,headers=dic_header).json()
# # # print(res['data'])
# # #
# # # 登陆小金体育
# # url3 = 'http://www.sport-server.top/sportApi/loginBackendAndXJ'
# # data3 = {"username":"auto123",
# #          "password":'auto123123'}
# # res2 = requests.post(url=url3,data=data3).json()
# # print(res2)
# # # print((res2['data']['uid']))
# #
# #
# # # 获取赛事列表
# # url4 = 'http://www.sport-server.top/sportApi/getMatch'
# # data4 ={
# #         "dataType":-2,
# #         "inPlay":True,
# #         "oddType":1,
# #         "pageNumber":0,
# #         "pageType":4,
# #         "sortBy":1,
# #         "sportId":[1]
# #         }
# # headers4 ={"Content-Type": "application/json"}
# # res4 = requests.post(url4,data=json.dumps(data4),headers=headers4).json()
# # print(res4)
# #
# #
# #
# # url5 = 'http://www.sport-server.top/sportApi/getMatchDetail'
# # # data5 = { "matchId":mid,
# # #           "inPlay":True,
# # #           "oddType":1
# # #          }
# # # headers5 ={'uid':str(res2['data']['uid'])}
# # # res5 = requests.post(url4,data=data5,headers=headers5).json()
# # # print(res5)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # #
# # # list_data = {"lma001": "1234qwer", "elma002": "1234qwer", "elma003": "1234qwer", "elma004": "1234qwer",
# # #              "elma005": "	1234qwer",
# # #              "elma006": "1234qwer", "elma007": "1234qwer", "rita27": "q12345678", "rita37": "q12345678",
# # #              "rita47": "	q12345678",
# # #              "rita57": "	q12345678", "rita67": "q12345678", "rita17": "q12345678", "rita87": "q12345678",
# # #              "rita99": "q12345678",
# # #              "fly111": "akl123456", "fly222": "akl123456", "hytest0": "a123456654321", "hytest2": "a123456654321",
# # #              "frank12345": "frank123}"
# # #              }
# # # print(len(list_data))
# # # for v,k in list_data.items():
# # #     print('{v}:{k}'.format(v = v, k = k))
#
# a = '1'
# b = '2'
# c ='12'
# print(a+b)

for i in range(2):
    print(i)
