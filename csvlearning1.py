import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) # redadr是一个可迭代体对象，每次返回list[str]
    # 读取表头
    header_row = next(reader) # 读取下一行，返回类型为list[str]
    print(header_row)
    
    # 读取表头索引和内容,
    for index, column_header in enumerate(header_row):
        print(str(index)+":"+column_header)

    # 读取第二列Max TemperatureF
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d") # 读取日期
        dates.append(current_date) # 将日期存储到列表中
        high = int(row[1]) # 读取最高温度
        highs.append(high) # 将最高温度存储到列表中
        low = int(row[3]) # 读取最低温度
        lows.append(low) # 将最低温度存储到列表中

# 创建图片
fig = plt.figure(figsize=(10, 6))
weather_fig = fig.subplots()
weather_fig.plot(dates, highs, c='red', alpha=0.7) # Alpha 值为0表示完全透明， 1（默认设置） 表示完全不透明。
weather_fig.plot(dates, lows, c='blue', alpha=0.7)

# 设置图形格式
fig.autofmt_xdate() # 旋转日期标签
weather_fig.set_title("Daily high and low temperatures-2014", fontsize=20)
weather_fig.set_ylabel("Temperature(F)", fontsize=16)
weather_fig.tick_params(axis='both', which='major', labelsize=10)
weather_fig.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # 给图表区域着色

# 显示图片
plt.show()

"""
1.这里解释一下参数类型：Iterable[str]，它表示每次输出为字符串对象的可迭代体对象，如列表，文件等。
2.重新认识列表和字典：list是一个可以存放任意对象（如str, int, 自定义对象）的对象，同样字典中的值也可以是任意对象
"""