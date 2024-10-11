import matplotlib.pyplot as plt

# 如果指定横坐标，横坐标从0开始
input_values = [1, 2, 3, 4, 5]
squares1 = [1, 4, 9, 16, 25]

plt.plot(input_values, squares1, linewidth=5)

# 设置图表标题， 并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Suqare of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=10)

plt.show()