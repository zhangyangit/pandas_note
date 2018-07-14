# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 02-Pandas基本功能详解
'''

import numpy as np
import pandas as pd

# 构建数据
index = pd.Index(data=['Tom', 'Sam', 'Jam', 'Lop'], name='name')
data = {
    'age': [10, 20, 30, 40],
    'city': ['NewYork', 'BeiJing', 'Paris', 'London'],
    'sex': ['male', 'male', 'female', 'male']
}

user_info = pd.DataFrame(data=data, index=index)
print(user_info)

## 常用功能
# 获取整体数据信息
print(user_info.info())
# 获取头部数据信息,head()、 tail()
print(user_info.head(2))
# 获取属性
print(user_info.shape)
# 获取转置
print(user_info.T)
# 获取源数据
print(user_info.values)

## 描述与统计
# max(最大) ,min（最小）, mean（评价）, quantile（中位数）, sum（求和）
# 对一个 Series 调用 这几个方法之后，返回的都只是一个聚合结果。
print(user_info.age.quantile())
# cumsum 累加求和的，也就是说它得到的结果与原始的 Series 或 DataFrame 大小相同。
print(user_info.age.cumsum())
print(user_info.sex.cumsum())
# 想要一次性获取多个统计指标，只需调用 describe 方法即可
# 总数， 平均数， 标准差， 最小值，最大值，25/50/75分位数，最大值
print(user_info.describe())
# 非数字类型的列的一些统计指标：总数，去重后的个数、最常见的值、最常见的值的频数
print(user_info.describe(include=['object']))
# 获取某列最大值或最小值对应的索引，可以使用 idxmax 或 idxmin 方法完成
print(user_info.age.idxmax())

## 离散化
# 自动分段  cut
print(pd.cut(user_info.age, 3))
# 按需分段
print(pd.cut(user_info.age, [1, 16, 29, 35, 49]))
# 按需分段,命名
print(pd.cut(user_info.age, [1, 16, 29, 35, 49], labels=['baby', 'child', 'girl', 'lady']))

# qcut
print(pd.qcut(user_info.age, 3))

## 排序
# 索引排序 sort_index
print(user_info.sort_index())
# 倒序排序 按照列进行倒序排，可以设置参数 axis=1 和 ascending=False ???
print(user_info.sort_index(axis=1, ascending=False))
# 按值排序
print(user_info.sort_values(by='age'))
# 按list 排序
print(user_info.sort_values(by=['age', 'city']))
# 获取排序成果 nlargest 和 nsmallest 方法来完成
print(user_info.age.nlargest(2))

## 函数应用
# 接收函数
print(user_info.age.map(lambda x: 'yes' if x >= 30 else 'no'))
#
city_map = {
    "BeiJing": "north",
    "NewYork": "south",
    "Paris": "south",
    "London": "south"
}
print(user_info.city.map(city_map))
print(user_info)

# apply
 # Series
print(user_info.age.apply(lambda x: 'yes' if x >= 30 else 'no'))
 # DataFrame
print(user_info.apply(lambda x: x.max(), axis=0))

# applymap
print(user_info.applymap(lambda x: str(x).lower()))

## 修改列、索引名称
user_info1 = user_info.rename(columns={"age": "Age", "city": "City", "sex": "Sex"})
print(user_info1)
print(user_info)

user_info2 = user_info.rename(index={"Tom": "tom", "Sam": "sam"})
print(user_info2)
print(user_info)

## 类型操作
# 获取每种类型的列数的话，可以使用 get_dtype_counts 方法。
print(user_info.get_dtype_counts())

# 转换类型
user_info3 = user_info["age"].astype(float)
print(user_info)
print(user_info3)

# 添加
user_info["height"] = ["178", "168", "178", "180cm"]
print(user_info)
# 错误处理
print(pd.to_numeric(user_info.height, errors='coerce'))
print(pd.to_numeric(user_info.height, errors='ignore'))