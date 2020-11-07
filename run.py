# -*coding:utf-8-*-
# @Time 2020/10/25 15:53
# @Author:TJX
# @Email:3033840048@qq.com
# @File:run.PY
# @Software:PyCharm
from python_class import lesson_5 #导入封装函数
from test_data import test_date  #导入测试数据
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
#从测试文档里面取测试数据
url=test_date.url["url"]
username=test_date.login_date["username"]
pwd=test_date.login_date["password"]
s_key=test_date.s_key["s_key"]
#函数的调用和传参
#给函数定义了一个返回值--调用的时候用一个变量进行接收
num=lesson_5.search_key(url=url,driver=driver,username=username,password=pwd,s_key=s_key) #通过关键字传参
if "314" in num:
    print("单据编号是:{}".format(num))
else:
    print("这条测试用例不通过")