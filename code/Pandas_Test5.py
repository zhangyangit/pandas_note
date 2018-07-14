# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 05-Pandas分类数据详解
'''
import numpy as np
import pandas as pd
from pandas.api.types import union_categoricals
# 分类数据直白来说就是取值为有限的，或者说是固定数量的可能值。
index = pd.Index(data=["Tom", "Bob", "Mary", "James", "Andy", "Alice"], name="name")
user_info = pd.Series(data=["A", "AB", np.nan, "AB", "O", "B"], index=index, name="blood_type", dtype="category")
print(user_info)

# 使用 pd.Categorical 来构建分类数据。
print(pd.Categorical(['A', 'AB', np.nan, 'AB', 'O', 'B']))
print(pd.Categorical(['A', 'AB', np.nan, 'AB', 'O', 'B'], categories=['A', 'B', 'AB']))

# 对于 Series 对象，使用astype 转换分类数据
user_info1 = pd.Series(data=["A", "AB", np.nan, "AB", "O", "B"], index=index, name="blood_type")
user_info1 = user_info.astype("category")
print(user_info1)

## 常用操作
# 分类数据使用 .describe() 方法，它得到的结果与 string类型的数据相同
# count 表示非空的数据有5条，unique 表示去重后的非空数据有4条，top 表示出现次数最多的值为 AB，freq 表示出现次数最多的值的次数为2次。
print(user_info.describe())
# 使用 .cat.categories 来获取分类数据所有可能的取值
print(user_info.cat.categories)

# 重命名
print(user_info.cat.rename_categories(['A+', 'AB+', 'B+', 'O+']))
# 数据分布
print(user_info.value_counts())
# 属性访问
print(user_info.str.contains('A'))
# 数据合并
blood_type1 = pd.Categorical(["A", "AB"])
blood_type2 = pd.Categorical(["B", "O"])
print(pd.concat([pd.Series(blood_type1), pd.Series(blood_type2)]))
# 合并数据并保持 分类类型
print(union_categoricals([blood_type1, blood_type2]))

## 内存使用量的陷阱
# Categorical 的内存使用量是与分类数乘以数据长度成正比，object 类型的数据是一个常数乘以数据的长度。

blood_type = pd.Series(['AB', 'A'])
blood_type1 = pd.Series(['AB', 'A']*1000)
blood_type2 = pd.Series(['A'])
print(blood_type.nbytes)
print(blood_type1.nbytes)
print(blood_type2.nbytes)
print(blood_type1.astype('category').nbytes)