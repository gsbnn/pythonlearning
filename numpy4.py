import numpy as np
#矩阵操作

#矩阵乘法
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

#矩阵转置
x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"

#矩阵与向量相加
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

#提取对角线元素
x = np.arange(9).reshape((3,3))     # Prints "[[0, 1, 2],
                                    #          [3, 4, 5],
                                    #          [6, 7, 8]]"

y = x.diagonal()        # y是只读的
print(np.diag(x))       # Prints "[0, 4, 8]"
print(np.diag(x,k=1))   # Prints "[1, 5]"
print(np.diag(x,k=-1))  # Prints "[3, 7]"

#构造对角线元素矩阵
print(np.diag(np.diag(x)))      # Prints "[[0, 0, 0],
                                #          [0, 4, 0],
                                #          [0, 0, 8]]"

#输出下三角
x = np.arange(3*4*5).reshape(3, 4, 5)       # x = "[[[ 0  1  2  3  4]
                                            #        [ 5  6  7  8  9]
                                            #        [10 11 12 13 14]
                                            #        [15 16 17 18 19]]

                                            #       [[20 21 22 23 24]
                                            #        [25 26 27 28 29]
                                            #        [30 31 32 33 34]
                                            #        [35 36 37 38 39]]

                                            #       [[40 41 42 43 44]
                                            #        [45 46 47 48 49]
                                            #        [50 51 52 53 54]
                                            #        [55 56 57 58 59]]]"
#将这个三维数组描述成：3组，4行，5列

print(np.tril(x))                           # Prints "[[[ 0  0  0  0  0]
                                            #           [ 5  6  0  0  0]
                                            #           [10 11 12  0  0]
                                            #           [15 16 17 18  0]]

                                            #          [[20  0  0  0  0]
                                            #           [25 26  0  0  0]
                                            #           [30 31 32  0  0]
                                            #           [35 36 37 38  0]]

                                            #          [[40  0  0  0  0]
                                            #           [45 46  0  0  0]
                                            #           [50 51 52  0  0]
                                            #           [55 56 57 58  0]]]"

#输出上三角
print(np.triu(x))
