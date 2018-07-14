# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 03-Pandas缺失值处理
'''
import numpy as np
import pandas as pd
### 导入
index = pd.Index(data=["Tom", "Bob", "Mary", "James", "Andy", "Alice"], name="name")

data = {
    "age": [18, 30, np.nan, 40, np.nan, 30],
    "city": ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen", np.nan, " "],
    "sex": [None, "male", "female", "male", np.nan, "unknown"],
    "birth": ["2000-02-10", "1988-10-17", None, "1978-08-08", np.nan, "1988-10-17"]
}

user_info = pd.DataFrame(data=data, index=index)

# 将出生日期转为时间戳
user_info["birth"] = pd.to_datetime(user_info.birth)
print(user_info)
# 其中 None， NAN，属于缺失值，

# 发现 None
print(user_info.isnull())

# 过滤 None
print(user_info[user_info.age.notnull()])

## 丢弃缺失值
print(user_info.age.dropna())
print(user_info)
# Seriese 使用 dropna 比较简单，对于 DataFrame 来说，可以设置更多的参数。
# axis 参数用于控制行或列，跟其他不一样的是，axis=0 （默认）表示操作行，axis=1 表示操作列。
# how 参数可选的值为 any（默认） 或者 all。any 表示一行/列有任意元素为空时即丢弃，all 一行/列所有值都为空时才丢弃。
# subset 参数表示删除时只考虑的索引或列名。
# thresh参数的类型为整数，它的作用是，比如 thresh=3，会在一行/列中至少有 3 个非空值时将其保留。
    # 一行数据只要有一个字段存在空值即删除
print(user_info.dropna(axis=0, how='any'))

    # 一行数据所有字段都为空值才删除
print(user_info.dropna(axis=0, how="all"))

    # 一行数据中只要 city 或 sex 存在空值即删除
print(user_info.dropna(axis=0, how="any", subset=["city", "sex"]))


## 填充缺失值
# 使用一个标量来填充
print(user_info.age.fillna(0))
print(user_info)
# 设置参数 method='pad' 或 method='ffill' 可以使用前一个有效值来填充
print(user_info.age.fillna(method="ffill"))
# 设置参数 method='bfill' 或 method='backfill' 可以使用后一个有效值来填充
print(user_info.age.fillna(method="backfill"))
# interpolate 方法来填充。默认情况下使用线性差值，可以是设置 method 参数来改变方式
print(user_info.age.interpolate())

## 替换缺失值
# replace 替换缺失值
print(user_info.age.replace(40, np.nan))
# 映射字典
print(user_info.age.replace({40: np.nan}))
print(user_info.replace({40: np.nan}))
# 替换指定值
print(user_info.replace({"age": 40, "birth": pd.Timestamp("1978-08-08")}, np.nan))
# 特定字符串替换
print(user_info.sex.replace('unknown', np.nan))
# 正则替换
print(user_info.city.replace(r'\s+', np.nan, regex=True))


## 使用其他对象填充
age_new = user_info.age.copy()
#  inplace=True 修改到Series中去
age_new.fillna(20, inplace=True)
print(age_new)
print(user_info.age.combine_first(age_new))
print(user_info)
