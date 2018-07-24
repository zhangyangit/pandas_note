这是一份关于 Pandas 的系列教程，包含了 Pandas 中的各个方面。

Fork from AI派

# Version

- Python 3.6.4
- Pandas 0.20.3

# 目录

- [x] [Pandas数据结构详解](notebook/01-Pandas数据结构详解.ipynb)
- [x] [Pandas基本功能详解](notebook/02-Pandas基本功能详解.ipynb)
- [x] [Pandas缺失值处理](notebook/03-Pandas缺失值处理.ipynb)
- [x] [Pandas文本数据处理](notebook/04-Pandas文本数据处理.ipynb)
- [x] [Pandas分类数据详解](notebook/05-Pandas分类数据详解.ipynb)
- [x] [Pandas时间序列详解](notebook/06-Pandas时间序列详解.ipynb)
- [x] [Pandas计算工具介绍](notebook/07-Pandas计算工具介绍.ipynb)
- [x] [Pandas筛选操作详解](notebook/08-Pandas筛选操作详解.ipynb)
- [ ] [Pandas分组聚合详解](#目录)
- [ ] [Pandas转换连接详解](#目录)
- [ ] [Pandas重塑与透视表详解](#目录)
- [ ] [Pandas IO操作详解](#目录)
- [ ] [Pandas可视化详解](#目录)

# 更多

欢迎 Star 和 Fork ，如果想学习更多关于人工智能相关的知识，欢迎关注公众号：**AI派**。

![](image/公众号—AI派.jpg)

# code
目前相关涉及模块都已经练习完毕

# Program
1. 这些对 Series and DataFrame 的修改，有哪些是能够直接修改到源数据，那些需要重新赋值到其他对象
2. 对于内存陷阱，有些不理解：
	A： Series 一个占据8字节，这个是怎么定义的
	B： 为什么 Categorical 这个 会节省这么多的数据
	C： Categorical 的内存使用量是与分类数乘以数据长度成正比，不是很理解