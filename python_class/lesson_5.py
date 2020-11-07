# -*coding:utf-8-*-
# @Time 2020/10/25 15:08
# @Author:TJX
# @Email:3033840049@qq.com
# @File:lesson_5.PY
# @Software:PyCharm
import time #导入time模块
def login_page(username,password,driver): #登录
    driver.find_element_by_id("username").send_keys(username) #找到id为username的元素，进行传参
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver): #打开网页
    driver.get(url)
    driver.maximize_window()
def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    time.sleep(5)
    user = driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text
    if user == "测试用户":
        print("这个用户是:{}".format(user))
    else:
        print("这条测试用例不通过")
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    p_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    f_id=p_id+"-frame"
    driver.switch_to_frame(f_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)  # 找不到页面元素时可以强制等待
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text
    return num
