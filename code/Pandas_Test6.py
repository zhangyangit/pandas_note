# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Notes | 06-Pandas时间序列详解
'''
import numpy as np
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import *

# 在做金融领域方面的分析时，经常会对时间进行一系列的处理。Pandas 内部自带了很多关于时间序列相关的工具，所以它非常适合处理时间序列。在处理时间序列的的过程中，我们经常会去做以下一些任务：
# 生成固定频率日期和时间跨度的序列
# 将时间序列整合或转换为特定频率
# 基于各种非标准时间增量（例如，在一年的最后一个工作日之前的5个工作日）计算“相对”日期，或向前或向后“滚动”日期
# 使用 Pandas 可以轻松完成以上任务。

# 基础概述
# 下面列出了 Pandas中 和时间日期相关常用的类以及创建方法。

#    类	            备注	            创建方法
# Timestamp	        时刻数据	        to_datetime，Timestamp
# DatetimeIndex 	Timestamp的索引 	to_datetime，date_range，DatetimeIndex
# Period	        时期数据	        Period
# PeriodIndex	    Period	            period_range，PeriodIndex
# Pandas 中关于时间序列最常见的类型就是时间戳（Timestamp）了，创建时间戳的方法有很多种，我们分别来看一看。
# 创建时间戳
print(pd.Timestamp(2018, 7, 15))
print(pd.Timestamp('2018-7-15'))
# 时间跨度
print(pd.Period('2018-07'))
print(pd.Period('2018-07', freq='D'))
# Timestamp 和 Period 可以是索引。
# 将Timestamp 和 Period 作为 Series 或 DataFrame 的索引后会自动强制转为为 DatetimeIndex 和 PeriodIndex
dates = [pd.Timestamp('2018-07-15'), pd.Timestamp('2018-07-14'), pd.Timestamp('2018-07-13'), pd.Timestamp('2018-07-12')]
ts = pd.Series(data=['Tom', 'Jam', 'Sam', 'Ham'], index=dates)
print(ts.index)

periods = [pd.Period('2018-07'), pd.Period('2018-06'), pd.Period('2018-05'), pd.Period('2018-04')]
ts = pd.Series(data=['Tom', 'Jam', 'Sam', 'Ham'], index=periods)
print(ts.index)

## 转换时间戳
# 通过 to_datetime 能快速将字符串转换为时间戳。当传递一个Series时，它会返回一个Series（具有相同的索引），而类似列表的则转换为DatetimeIndex
# (1)
print(pd.to_datetime(pd.Series(['Jul 31, 2018', '2018-07-15', None])))
# (2)
print(pd.to_datetime(['2018/7/25', '2018.7.15']))
# (3) Linux 时间
print(pd.to_datetime([1349720105, 1349806505, 1349892905], unit='s'))
# (4)
print(pd.to_datetime([1349720105100, 1349720105200, 1349720105300], unit="ms"))

## 生成时间戳的范围
# (1)
print(pd.date_range('2018-7-15', periods=8))
# (2)
print(pd.bdate_range('2018-7-15', periods=8))
# (3)date_range 默认使用的频率是 日历日，而 bdate_range 默认使用的频率是 营业日。
# 当然了，我们可以自己指定频率，比如，我们可以按周来生成时间戳范围
print(pd.date_range('2018-7-15', periods=8, freq='W'))

## DatetimeIndex
# DatetimeIndex 的主要作用是之一是用作 Pandas 对象的索引，
# 使用它作为索引除了拥有普通索引对象的所有基本功能外，还拥有简化频率处理的高级时间序列方法。
# (1)
rng = pd.date_range('2018-6-24', periods=4, freq='W')
ts = pd.Series(range(len(rng)), index=rng)
print(ts)
# (2)
print(ts['2018-07-08'])
# (3)
print(ts['2018-07-08': '2018-07-22'])
# (4)将日期作为参数，还可以将年份或者年份、月份作为参数来获取更多的数据
print(ts['2018'])
# (5)
print(ts['2018-07'])
# (6)
print(ts[datetime(2018, 7, 8): datetime(2018, 7, 22)])
# (7)
print(ts.index.year)
print(ts.index.dayofweek)
print(ts.index.weekofyear)

## DateOffset 对象
d = pd.Timestamp('2018-06-25')
print(d + DateOffset(weeks=2, days=5))

## 与时间序列相关的方法
# (1) 移动
print(ts.shift(2))
# (2) freq
print(ts.shift(2, freq=Day()))
# (3)
print(ts.tshift(2, freq=Day()))

## 频率转换
print(ts.asfreq(Day()))
# 填充
print(ts.asfreq(Day(), method='pad'))

## 重采样
print(ts.resample('1M').sum())
print(ts.resample('1M').mean())














