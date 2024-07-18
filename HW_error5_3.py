import numpy as np

L = np.array([43.61, 43.63, 43.68, 43.71, 43.74, 43.78]).reshape(6,1)
print(L)

A = np.array([[1, 15],[1, 18],[1, 21],[1, 24],[1, 27],[1, 30]])
C_inv = np.linalg.inv(np.dot(A.T, A))
print(C_inv)
CinvAt = np.dot(C_inv,A.T)
X = np.dot(CinvAt,L)
print(X)

V = L - np.dot(A,X)
print(V)
oF = np.sqrt(np.sum(V**2)/4)
print(oF)
