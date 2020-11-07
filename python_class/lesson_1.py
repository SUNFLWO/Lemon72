# -*coding:utf-8-*-
# @Time 2020/10/12 20:45
# @Author:TJX
# @Email:3033840049@qq.com
# @File:lesson_1.PY
# @Software:PyCharm
# print("hello world")
# 标识符的命名
# （1）只能包含数字、字母、下划线这三种，不能有其他
# （2）不能以数字开头
# （3）不能用关键字--keyword
# print 打印内容到控制台
# import keyword
# print(keyword.kwlist)
# 注释:解释说明，方便阅读；功能不影响现有的运行 ，且能保存
'''print("1")
 print("hello world")'''

# print(type(12))
# print(isinstance("hello",str))
#
# print('''nisd'黎明'jSD''')
# print('''----黎明-----
#   name:黎明
#      age:18
#       hobby:看书
# ''')
# print(type(3.1412))
# pan=1

# 变量:用来存储数据 见名知意
# 变量名一定要先申明(定义并赋值)
info='这是美丽的女孩!'
# name="彩虹"
# print(name)
# print(info)
str1="hello world"
# print(str1[2:5:2])
# print(str1[::])
# str1=str1.replace("world","yes")
print(str1)
# print(str1.index("G")) #如果元素没有找到，会报错，代码终止
print(str1.find("G")) #如果元素没有找到，不会报错，返回-1
#
# name="锋行"
# age=18
# hobby="唱歌"
# print('''----{0}----
# name:{1}
# age:{2}
# hobby:{3}
# '''.format(name,name,age,hobby))

# print(10+20) #两个数字的相加
# print("hello"+"world") #两个字符串的相加
# print(str(123)+"abc") #强制字符串转换
# print(30-10) #两个数字相减
# print(2*3) #两个数字相乘
# print("love yun "*30) #字符串的重复输出
# print(10/3) #结果浮点型
# print(11%4) #取余
#
# a=10
# b=20
# a+=10
# a-=5
# print(a)
# print(a<b)
# print(a==b)
# name=input("请输入姓名:")
# age=input("请输入年龄:")
# sex=input("请输入性别:")
# print('''*************
# 姓名:{}
# 性别:{}
# 年龄:{}
# *************'''.format(name,age,sex))

str1 = 'python hello aaa 123123aabb'
# print(str1[:6:1])
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)
'''str1=str1.replace("python","lemon")'''
print(str1)
print(str1.index("aaa"))