# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 01-Pandas数据结构详解
'''
import numpy as np
import pandas as pd

### Series
user_age = pd.Series(data=[19, 30, 21, 32])
user_age.index = ['Tom', 'Jam', 'Sam', 'Ham']
user_age.index.name = 'name'
user_age.name = 'user_info'
print(user_age)
## 创建 pandas 数据类型
name1 = pd.Index(['Pam', 'Mam', 'Nam', 'Tam'], name='name')
user_age1 = pd.Series([10, 11, 12, 13], index=name1, name='user_info', dtype=float)
print(user_age1)

## 数据操作
print('operation')
print(user_age1.get('Tam'))
# 按坐标取值
print(user_age1[1])
# 切片
print(user_age1[:3])
# 运算符
print(user_age1[ user_age1 > 11])
# 定点
print(user_age1[[1, 3]])
# 向量化操作
print('Vector')
print(user_age1 + 1)
# exp
print(np.exp(user_age1))

### DataFrame
# DataFrame 是一个带有**索引**的二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。
# 你可以把它想象成一个 excel 表格或者数据库中的一张表，DataFrame 是最常用的 pandas 对象。
## 创建数据对象
index = pd.Index(data=['Tom', 'Jam', 'Sam', 'Lom'], name='name')
data = {
    'age': [10, 20, 30, 40],
    'city': ['WuHan', 'ShangHai', 'GuangZhou', 'ShenZhen']
}
user_info = pd.DataFrame(data=data, index=index)
print(user_info)

data = [
    [10, 'Beijing'],
    [20, 'WuHan'],
    [30, 'TianJin'],
    [40, 'ShenZhen']
]
columns = ['age', 'city']
user_info1 = pd.DataFrame(data=data, index=index, columns=columns)
print(user_info1)

## 数据操作
# 访问行
print(user_info1.loc['Tom'])
# 选择行
print(user_info1.iloc[0])
# 切片
print(user_info1.iloc[1:3])
# 访问列
print(user_info1.age)
print(user_info1['age'])
print(user_info1[["city", "age"]])
# 增加/删除列
user_info1["sex"] = "male"
print(user_info1)
# pop 删除
user_info1.pop("sex")
print(user_info1)
user_info1["sex"] = ["male", "male", "female", "male"]
print(user_info1)
# 保证原有的 DataFrame 不改变的话，我们可以通过 assign 方法来创建新的一列
print(user_info1.assign(age_add_one = user_info["age"] + 1))
print(user_info1)
print(user_info1.assign(sex_code=np.where(user_info1['sex'] == 'male', 1, 0)))
print(user_info1)