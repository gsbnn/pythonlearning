import matplotlib.pyplot as plt
# 绘制散点图 plt.scatter()

x_values = range(1,1000)
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# 设置每个坐标轴的取值范围
plt.axis((0, 1100, 0, 1100000))

plt.show()
