# -*coding:utf-8-*-
# @Time 2020/10/19 17:36
# @Author:TJX
# @Email:3033840049@qq.com
# @File:lesson_3.PY
# @Software:PyCharm
# for循环:遍历 数据对象里面的所有元素:str,list,tuple,dict
# for 变量名 in 数据对象:
#     子代码（循环体）
#  循环多少次由什么决定的--元素的个数
# count=0 #计数器
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# for name in list1:
#     if name =="荷花鱼":
#       #break  #跳出整个循环
#       continue #跳出本次循环
#     print(name)
#     print("*"* 20)
#     count += 1
# print(count)
# print(len(list1))

# range()函数:生成一个整数序列 1,2,3,4,5,6
# for i in range(0,6,2): #开始 结束 步长
#     print(i)
# 函数:封装成函数，调用。==提高代码的复用率，提高执行的效率
# 语法：
# def 函数名():
#    子代码（函数体）--实现功能
# 1.形参--函数定义的时候定义
# 2.实参--调用函数传入参数
# def good_job(salary,bonus,subsidy):
#     sum1=salary+bonus+subsidy
#     print("这个工作的工资总和是{}".format(sum1))
# good_job(8000,2000,500)

# 参数定义的类型:
# 1.必备参数:定义了就必须要传入的参数
# 2.默认参数（缺省参数）:可以定义的时候赋值一个默认值--调用的时候可以不传入;传入时，替换掉默认参数
# def good_job(salary,bonus,subsidy=500):
#  sum1=salary+bonus+subsidy
#  print("这个工作的工资总和是:{}".format(sum1))
# good_job(8000,2000,300)
# 3.不定长参数(*args):等前面的必备参数都接收完了，才进行不定长参数的传参 否则后面有必备参数时会报错
# 接收不确定数量，个数的参数--可以不传，可以传入（1个、多个）==元祖接收  *args会在他所在的位置进行所有参数的接收
# def good_job(salary,bonus,subsidy=500,*args):
#  sum1=salary+bonus+subsidy
#  print("args的值是:{}".format(args))
#  for i in args:
#      sum1+=i
#  print("这个工作的工资总和是:{}".format(sum1))
# good_job(8000,2000,300,50,100,200)

# 4.传参的方式类型:
# (1)位置传参:按照位置参数传入
# (2)关键字传参:指定参数名来进行传参，不关心顺序
# (3)混合传参:关键字传参必须跟在位置传参后面
# def good_job(salary, bonus, subsidy=500, *args):
#  sum1=salary+bonus+subsidy
#  print("args的值是:{}".format(args))
#  for i in args:
#      sum1+=i
#  print("这个工作的工资总和是:{}".format(sum1))
# good_job(8000,bonus=2000,subsidy=300)

# 5.不定长传参:**kwargs 按照关键字进行传参，进行不定长参数的接收，==字典的接收方式 关键字后面不能再传参
# def good_job(salary, bonus, subsidy=500, *args,**kwargs):
#  sum1=salary+bonus+subsidy
#  print("args的值是:{}".format(args))
#  print("kwargs的值是:{}".format(kwargs))
#  for i in args:
#      sum1+=i
#  for j in kwargs: #字典取值 kwargs[j]/kwargs.get[j]
#      sum1+=kwargs[j]
# print("这个工作的工资总和是:{}".format(sum1))
# good_job(8000,2000,300,50,100,200,aa=50,bb=80,cc=100,dd=120)

# 6.函数的返回值: 有进有出 进--传入的参数， 出--返回值
# 返回值:函数可以给到外面的人用的数据--调用函数的时候，可以获取到这个返回值--return
# (1)定义
# (2)调用--变量接收返回值,多个时用元组进行返回接收
# (3)如果没有返回值--None
#（4）返回值写在函数的最后--标志着函数的结束
# def good_job(salary, bonus, subsidy=500, *args,**kwargs):
#   sum1=salary+bonus+subsidy
#   print("args的值是:{}".format(args))
#   print("kwargs的值是:{}".format(kwargs))
#   for i in args:
#       sum1+=i
#   for j in kwargs: #字典取值 kwargs[j]/kwargs.get[j]
#      sum1+=kwargs[j]
#   return sum1,salary
# result=good_job(8000,2000,800) #定义一个变量去进行函数返回值的接收
#   # if result>10000:
#   #   print("这是一个不错的工作")
#   # else:
#   #  print("我还可以找到更好的工作")
# print(result)
def sum1(n):
   sum=0
   for i in range(n):
     sum+=i
   print(sum)
sum1(100)

def yes(object):
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        lenth = len(object)
        if lenth>5:
           print("True")
        else:
           print("False")
    else:
        print("该数据类型不支持计算长度")
yes([1,2,3,"yun"])
