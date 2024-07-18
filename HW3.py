import numpy as np
import matplotlib.pyplot as plt

P = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
V1 = np.array([3.25, 3.44, 3.59, 3.77, 3.93, 4.12, 4.27, 4.46, 4.62, 4.8, 4.95])
V2 = np.array([3.23, 3.4, 3.57, 3.75, 3.92, 4.1, 4.27, 4.45, 4.61, 4.79, 4.97])
ave_V = (V1 + V2)/2
P = P*1000
print(ave_V)

fit_cofficient = np.polyfit(P, ave_V, 1)
fit_line = np.poly1d(fit_cofficient)
fit_point = fit_line(P)
max_error = np.max(np.abs(fit_point - ave_V))
error_relative = max_error/(fit_point[-1]-fit_point[0])*100
print(fit_cofficient)
print(fit_point)
print(max_error)
print(error_relative)

plt.plot(P,ave_V,'*')
plt.plot(P,fit_point)
plt.title("the characteristic curve of output voltage and input pressure")
plt.xlabel("input pressure/Pa")
plt.ylabel("output voltage/V")
text = 'y='+str(round(fit_cofficient[0],8)) + 'x+' + str(round(fit_cofficient[1],4))
print(text)
plt.text(6500,3.6,text,size = 10)
plt.savefig('test3.png')
plt.show()