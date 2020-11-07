# -*coding:utf-8-*-
# @Time 2020/10/14 23:28
# @Author:TJX
# @Email:3033840049@qq.com
# @File:lesson_2.PY
# @Software:PyCharm
# 常用数据类型续：列表 元组 字典  集合
# 列表(list):[],元素之间用英文逗号隔开
#  1.元素可以是任意的数据类型: int float bool str list...
#  2.取值:索引取值--类比字符串
#  取多个值:切片取值
#  列表的嵌套取值
List1 = [20, 3.14, True,'明白', [1, 2, 3, 4]]
# print(List1[0])
# print(List1[2:5:1])
# print(List1[4][2])

# 列表的元素是可以被改变的
# 增加
# List1.append("李白") #默认追加元素到列表的末尾
# List1.insert(5,"yes") #指定位置进行元素插入
# List1.extend(['yes',"黎明"]) #两个列表的合并
# print(List1)
# 删除
# List1.pop() # 默认删除最后一个元素,也可以指定位置进行删除
# List1.remove(3.14) # 指定元素本身进行删除
# print(List1)
# 修改  取值-重新赋值
# List1[2]="yun"
# List1[0]="123"
# print(List1)

# 列表元素可以重复  count可以统计元素个数
# List1.append("123")
# print(List1.count("123"))
# len 可以统计列表长度
# print(len(List1))

# 元组 tuple ()
# (1)元素可以是任意的数据类型:int float bool str list...
# tuple1=(20,3.14,True,"明白",[1,2,3,4])
# (2)取值:索引取值--类比字符串 tuple[2]
#   取多个值:切片取值 tuple1[2:5:1]
# (3)列表的嵌套取值 tuple1[4][2]
# (4)元组的元素是不可以被改变的
# (5)列表元素可以重复  count可以统计指定元素个数
# (6)len()--统计元素个数
# list1=list(tuple1)
# list1[1]="456"
# tuple2=tuple(list1)
# print(tuple2)


# 字典:dict {}
# 1.元素:key:value(键值对)
# 2.场景:存储数据属性: 人--名字 身高 体重
# key:1) 不能是可以改变的数据类型（list,dict)--字符串
#     2）不能重复的，唯一的
# value:可以是任意数据类型--可以被改变==增删改
# 3.字典是没有顺序的 ==不能索引取值 通过key 取value
# dict1={"name":"tan","height":"173","weight":"160"}
# print(dict1["height"])
# print(dict1.get("weight"))
# dict1["weight"]="150" #key存在，修改对应key的value
# dict1["age"]=18 #key不存在，新增加键值对
# print(dict1)

#删除
# dict1.pop("weight") #指定key删除 对应的键值对
# print(dict1)
# del dict1 #变量存储删除 --对象不存在了

# dict1.update({"city":"北京","hobby":"学习","sex":"male"}) #字典的合并
# print(dict1)

# 集合: set {},元素单个
# 1.无序
# 2.元素不可以重复--使用场景:去重
# list2=[11,22,11,33,11,11]
# set1=set(list2) #set() --list2转化为集合
# print(set1) #list() --set1 转化为列表
# list3=list(set1)
# print(list3)

# 控制流:代码的执行顺序--从上至下一次执行:判断 循环
# 判断: if 语法
# if 条件: ---成立---冒号:缩进（4个空格=tab键）
#     子代码（执行语言）
# elif 条件:--成立
#     执行语句（子代码）
# ...(可以没有，也可以有多个)
# else: --可以没有
#     执行语句
# money=int(input("请输入余额:"))
# if money>=500: #True
#     print("买别墅!")
# elif money>=200: #False
#     print("买一栋楼")
# elif money>=50:
#     print("买车")
# else:
#     print("滚去工作")

# a=[1,2,'6','summer']
# print("i"in a)
#
# dict_1={"class_id":45,'num':20}
# num=dict_1.get("num")
# if num>5:
# #     print(num)
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# dict_1={}
# list_2=['方方土','七木','荷花鱼','kingo','Amiee','焕蓝']
# list_3=["男","女","女","女","男","女"]
# list_4=[]
# list_5=[20,22,24,25,26,28]
# list_6=["武汉","上海","成都","深圳","河南","北京"]
# for i in range(len(list1)):
#     dict_1=dict(name=list_2[i],sex=list_3[i],age=list_5[i],city=list_6[i])
#     list_4.append(dict_1)
# print(list_4)
print(5/3)