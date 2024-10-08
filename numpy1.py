import numpy as np
#核心，一个多维数组对象
#创建数组对象：numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

#           参数说明

#   参数                说明
#   object	    数组或嵌套的数列
#   dtype	    数组元素的数据类型，可选
#   copy	    对象是否需要复制，可选
#   order	    创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
#   subok	    默认返回一个与基类类型一致的数组
#   ndmin	    指定生成数组的最小维度

#矩阵，二维数组，具有行和列；
#向量，看作只有一行或一列的矩阵


#切片
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]

#属性
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64，数组类型
print(a.size) # >>>25，数组元素个数
print(a.shape) # >>>(5, 5)，数组的行和列数
print(a.itemsize) # >>>8，数组一个元素占用字节数
print(a.ndim) # >>>2，数组的维度
print(a.nbytes) # >>>200，数组中的所有数据消耗掉的字节数


#切片不是复制，是原数组的引用
#改变切片，同时也改变了原数组
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]   # [[2 3]
                 #  [6 7]]

print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"

