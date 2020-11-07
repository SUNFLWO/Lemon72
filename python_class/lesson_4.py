# -*coding:utf-8-*-
# @Time 2020/10/20 17:54
# @Author:TJX
# @Email:3033840049@qq.com
# @File:lesson_4.PY
# @Software:PyCharm
'''web自动化:
代码  翻译(中间人)  浏览器
python ------->浏览器驱动 ------->调用相应的浏览器
'''
# selenium:Python的工具，三个部分
# (1)ide:录制脚本--用的少
# (2)webdriver:库--提供对网页的各种操作+结合语言使用
# (3)grid:分布式-用的少

# import selenium #导入库里面的所有东西
from selenium import webdriver #从selenium库导入浏览器驱动
import time #导入time模块
driver=webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待，默认等待10秒
#选择谷歌浏览器进行初始化,与浏览器进行沟通，创建一个会话session
# #1.打开一个指定的网址
# driver.get("http://120.78.128.25:8765/Index/login.html")
# #2.浏览器窗口最大化
# driver.maximize_window()
# #3.打开新页面
# time.sleep(2) #等待，默认秒
# driver.get("http://erp.lemfix.com/login.html")
# #4. 向前、退后、刷新
# time.sleep(2)
# driver.back() #退回上一个页面
# time.sleep(2)
# driver.forward() #前进到下一个界面
# time.sleep(2)
# driver.refresh() #刷新页面
# #5.退出
# driver.quit() #关闭驱动，session关闭
# #driver.close() #关闭当前窗口，不会退出会话

# 基础知识:web页面==HTML+CSS+Javascript
# html:标签语言 <标签名>值</标签名>==呈现页面内容
# css:页面布局设置，字体颜色， 字体大小样式
# JS:依据不同效果
# 元素的特征:根据页面设计规则，有些特征是唯一的==开发遵循了这个规则
#1. id :类比身份证号 ==仅限当前页面
#2.Xpath定位：
'''(1)绝对路径:/html/body/div/div/div[1]/a/b --根节点,顺序性,继承关系，==失效不用
   (2)相对路径:只靠自己的特征定位 //开头--加上我关心节点
      标签名+属性的方式辅助定位 //标签名[@属性名=属性值]
      //input[@id="username"]
   (3)层级定位://标签名[@属性名=属性值]//标签名[@属性名=属性值]
    //div[@class="login-logo"]//b
   (4)文本属性定位://b[text()="柠檬ERP"]
   (5)包含属性值://标签名[contains(@属性名/text(),属性值)]
   //input[contains(@class,"username")]
   //b[contains(text(),"柠檬")]
'''
# 可对页面进行对应的操作:
# 1.点击 click()
# 2.传值 send_keys()
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
# driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")
#3.获取页面文本 text()
'''但凡是切换了页面，页面没有加载完，元素不显示==最好加个等待
# (1)强制等待:time.sleep(5) ==没有完成等待时间，不往下执行
# (2)智能等待:
#    隐式等待:可以设置等待时间，在这个等待时间还没有结束之前元素找到了，不继续等待，继续执行下面的代码:--灵活
     注意:一个session里只执行一次
     显示等待:expected_condition  
'''
page_text=driver.find_element_by_xpath('//div[@class="login-logo"]//b').text
# page_title=driver.title #获取页面的标题
# print("页面的标题是:{}".format(page_title))
if page_text=="柠檬ERP":
    print("这个页面的标题是:{}".format(page_text))
else:
    print("这条测试用例不通过")
#判断测试用户
time.sleep(5)
user=driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text
if user=="测试用户":
    print("这个用户是:{}".format(user))
else:
    print("这条测试用例不通过")
#点击零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
#点击搜索
'''
1.识别是否有子页面的方式:页面层级里面出现iframe页面，就需要切换iframe才可以进行元素的定位。
2.怎么去切换:
 (1)找到这个iframe元素，切换 
 (2)切换三种方式
   1.通过id来切换,获取到属性
   2.通过元素定位(xpath)来切换iframe
   3.通过iframe的下标来进行切换
'''
#1.通过id进行iframe切换
# p_id=driver.find_element_by_xpath('//div[text()=" 零售出库"]/..').get_attribute("id")
# f_id=p_id+"-frame"
# driver.switch_to_frame(f_id)
# driver.find_element_by_id("searchNumber").send_keys("314")
#2.通过元素定位(xpath)来切换iframe
# driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(f_id)))
# driver.find_element_by_id("searchNumber").send_keys("314")
#3.通过iframe的下标来进行切换
driver.switch_to_frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
#点击查询
driver.find_element_by_id("searchBtn").click()
time.sleep(2) #找不到页面元素时可以强制等待
#找到单据编号
num=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text
if "314" in num:
    print("单据编号是:{}".format(num))
else:
    print("这条测试用例不通过")

'''
八大元素定位:id name xpath(相对路径(//标签名[@属性名=属性]）、层级定位、文本定位、contains)
三大等待-强制、隐式、显式
四大操作:click() send_keys() text get_attribute()
iframe:三大切换方式
'''
