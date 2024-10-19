from die import Die
import pygal

# 创建两个D6骰子
die_1 = Die() # 可以更改骰子的面数，如die_1 = Die(10)
die_2 = Die()
results = []

# 存储结果
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# 计算各点出现的次数
frequencies = []
min_result = 2
max_result = die_1.num_sides + die_2.num_sides
for value in range(min_result, max_result+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

# 对结果进行可视化
hist = pygal.Bar() #创建一个Bar实例

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(min_result,max_result+1)) # 设置横坐标
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies) # 添加标签和值
hist.render_to_file("dice_visual.svg") # 保存为svg文件