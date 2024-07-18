import numpy as np

#常用数组操作
import numpy as np 
a = np.array([[1.0, 2.0], [3.0, 4.0]]) 
b = np.array([[5.0, 6.0], [7.0, 8.0]]) 
sum = a + b 
difference = a - b 
product = a * b 
quotient = a / b 
#可见数组运算是对应元素运算，而不是矩阵运算

#特殊数组操作
a = np.arange(10)
print(a)
print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]

x = np.array([[1,2],[3,4]])
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

