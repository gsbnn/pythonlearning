import matplotlib.pyplot as plt
# 绘制散点图 plt.scatter()

x_values = range(1,1000)
y_values = [x**2 for x in x_values]

# 将参数c 设置成了一个 y 值列表， 并使用参数cmap 告诉pyplot 使用哪个颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)
# 设置每个坐标轴的取值范围
plt.axis((0, 1100, 0, 1100000))

plt.show()

'''
要修改数据点的颜色， 可向scatter() 传递参数c ， 并将其设置为要使用的颜色的名称， 如下所示：
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

要让程序自动将图表保存到文件中， 可将对plt.show() 的调用替换为对plt.savefig() 的调用：
plt.savefig('matplotlib2_plot.png', bbox_inches='tight')
第一个实参指定要以什么样的文件名保存图表， 这个文件将存储到scatter_squares.py所在的目录中； 
第二个实参指定将图表多余的空白区域裁剪掉。 如果要保留图表周围多余的空白区域， 可省略这个实参。
'''
