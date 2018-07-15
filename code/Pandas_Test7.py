# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 07-Pandas计算工具介绍
'''
import numpy as np
import pandas as pd

## 统计函数
index = pd.Index(data=["Tom", "Bob", "Mary", "James", "Andy", "Alice"], name="name")

data = {
    "age": [18, 40, 28, 20, 30, 35],
    "income": [1000, 4500 , 1800, 1800, 3000, np.nan],
}

df = pd.DataFrame(data=data, index=index)
print(df)

# (1)通过 cov 函数来求出年龄与收入之间的协方差，计算的时候会丢弃缺失值
print(df.age.cov(df.income))
# (2)通过 corr 函数来计算下它们之间的相关性，计算的时候会丢弃缺失值
# 默认情况下 corr 计算相关性时用到的方法是 pearson，当然了你也可以指定 kendall 或 spearman
print(df.age.corr(df.income))
# (3)
print(df.age.corr(df.income, method='kendall'))
# (4)
print(df.age.corr(df.income, method='spearman'))
# (5) 通过 rank 函数求出数据的排名顺序
print(df.income.rank())
# (6) 默认取其排名的平均值作为值。我们可以设置参数来得到不同的结果。可以设置的参数有：min、max、first、dense
print(df.income.rank(method='first'))


## 窗口函数

data = {
    "turnover": [12000, 18000, np.nan, 12000, 9000, 16000, 18000],
    "date": pd.date_range("2018-07-01", periods=7)
}

df2 = pd.DataFrame(data=data)
print(df2)

# (1) 通过 rolling 我们可以实现，设置 window=2 来保证窗口长度为 2，设置 on="date"
# 来保证根据日期这一列来滑动窗口（默认不设置，表示根据索引来滑动
print(df2.rolling(window=2, on='date').sum())
# (2) 有很多结果是缺失值，导致这个结果的原因是因为在计算时，
# 窗口中默认需要的最小数据个数与窗口长度一致，这里可以设置 min_periods=1 来修改下。
print(df2.rolling(window=2, on='date', min_periods=1).sum())
# (3) 计算每段时间的累加和，如何实现呢？先来看看第一种方式吧
print(df2.rolling(window=len(df2), on='date', min_periods=1).sum())
# (4) 使用 expanding 来生成窗口
print(df2.expanding(min_periods=1)['turnover'].sum())

# (5) 可以使用 sum 函数外，还有很多其他的函数可以使用，如：
# 方法	        描述
# count()	    非空观测值数量
# sum()	        值的总和
# mean()	    价值的平均值
# median()	    值的算术中值
# min()	        最小值
# max()	        最大
# std()	        贝塞尔修正样本标准差
# var()	        无偏方差
# skew()	    样品偏斜度（三阶矩）
# kurt()	    样品峰度（四阶矩）
# quantile()	样本分位数（百分位上的值）
# apply()	    通用适用
# cov()	        无偏协方差（二元）
# corr()	    相关（二进制

# (6) 生成多个结果
print(df2.rolling(window=2, min_periods=1)['turnover'].agg([np.sum, np.mean]))

# (7) 重命名
print(df2.rolling(window=2, min_periods=1)['turnover'].agg({"tur_sum": np.sum, "tur_mean":np.mean}))