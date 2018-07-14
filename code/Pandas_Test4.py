# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 04-Pandas文本数据处理
'''
import numpy as np
import pandas as pd
### 引入
index = pd.Index(data=["Tom", "Bob", "Mary", "James", "Andy", "Alice"], name="name")

data = {
    "age": [18, 30, np.nan, 40, np.nan, 30],
    "city": ["Bei Jing ", "Shang Hai ", "Guang Zhou", "Shen Zhen", np.nan, " "],
    "sex": [None, "male", "female", "male", np.nan, "unknown"],
    "birth": ["2000-02-10", "1988-10-17", None, "1978-08-08", np.nan, "1988-10-17"]
}

user_info = pd.DataFrame(data=data, index=index)

# 将出生日期转为时间戳
user_info["birth"] = pd.to_datetime(user_info.birth)
print(user_info)

#
print(user_info.city.str.lower())
print(user_info.city.str.len())

## 替换与分隔
# 将空字符串替换成下划线。
print(user_info.city.str.replace(" ", "_"))
# replace 方法还支持正则表达式，例如将所有开头为 S 的城市替换为空字符串
print(user_info.city.str.replace("^S.*", " "))
# 根据空字符串来分割某一列
print(user_info.city.str.split(" "))
# 分割列表中的元素可以使用 get 或 [] 符号进行访问
print(user_info.city.str.split(" ").str.get(1))
# 设置参数 expand=True 可以轻松扩展此项以返回 DataFrame
print(user_info.city.str.split(" ", expand=True))

## 提取子串
# 提取第一个匹配的子串
# extract 方法接受一个正则表达式并至少包含一个捕获组，指定参数 expand=True 可以保证每次都返回 DataFrame
print(user_info.city.str.extract('(\w+)\s+', expand=True))
# 如果使用多个组提取正则表达式会返回一个 DataFrame，每个组只有一列。
print(user_info.city.str.extract('(\w+)\s+(\w+)', expand=True))

# 匹配所有字符串
# extract 只能够匹配出第一个子串，使用 extractall 可以匹配出所有的子串。
print(user_info.city.str.extractall('(\w+)\s+'))
# 使用 contains 来测试是否包含子串
print(user_info.city.str.contains('Zh'))

# 生成哑变量
# get_dummies 方法可以将字符串转为哑变量，sep 参数是指定哑变量之间的分隔符
print(user_info.city.str.get_dummies(sep=' '))

#
#方法摘要
#这里列出了一些常用的方法摘要。

#方法	描述
#cat()	连接字符串
#split()	在分隔符上分割字符串
#rsplit()	从字符串末尾开始分隔字符串
#get()	索引到每个元素（检索第i个元素）
#join()	使用分隔符在系列的每个元素中加入字符串
#get_dummies()	在分隔符上分割字符串，返回虚拟变量的DataFrame
#contains()	如果每个字符串都包含pattern / regex，则返回布尔数组
#replace()	用其他字符串替换pattern / regex的出现
#repeat()	重复值（s.str.repeat(3)等同于x * 3 t2 >）
#pad()	将空格添加到字符串的左侧，右侧或两侧
#center()	相当于str.center
#ljust()	相当于str.ljust
#rjust()	相当于str.rjust
#zfill()	等同于str.zfill
#wrap()	将长长的字符串拆分为长度小于给定宽度的行
#slice()	切分Series中的每个字符串
#slice_replace()	用传递的值替换每个字符串中的切片
#count()	计数模式的发生
#startswith()	相当于每个元素的str.startswith(pat)
#endswith()	相当于每个元素的str.endswith(pat)
#findall()	计算每个字符串的所有模式/正则表达式的列表
#match()	在每个元素上调用re.match，返回匹配的组作为列表
#extract()	在每个元素上调用re.search，为每个元素返回一行DataFrame，为每个正则表达式捕获组返回一列
#extractall()	在每个元素上调用re.findall，为每个匹配返回一行DataFrame，为每个正则表达式捕获组返回一列
#len()	计算字符串长度
#strip()	相当于str.strip
#rstrip()	相当于str.rstrip
#lstrip()	相当于str.lstrip
#partition()	等同于str.partition
#rpartition()	等同于str.rpartition
#lower()	相当于str.lower
#upper()	相当于str.upper
#find()	相当于str.find
#rfind()	相当于str.rfind
#index()	相当于str.index
#rindex()	相当于str.rindex
#capitalize()	相当于str.capitalize
#swapcase()	相当于str.swapcase
#normalize()	返回Unicode标准格式。相当于unicodedata.normalize
#translate()	等同于str.translate
#isalnum()	等同于str.isalnum
#isalpha()	等同于str.isalpha
#isdigit()	相当于str.isdigit
#isspace()	等同于str.isspace
#islower()	相当于str.islower
#isupper()	相当于str.isupper
#istitle()	相当于str.istitle
#isnumeric()	相当于str.isnumeric
#isdecimal()	相当于str.isdecimal













