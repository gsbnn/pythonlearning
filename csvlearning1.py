import csv
from datetime import datetime
from matplotlib import pyplot as plt

def read_tempture(tempture_file):
    """读取温度和日期，tempture_file是csvfile_path"""
    with open(tempture_file) as f:
        # 创建csv迭代体
        reader = csv.reader(f) # 返回一个csv迭代体对象,每次迭代输出csv文件的一行
        
        # 读取表头
        header_row = next(reader) # # 读取迭代体的一次迭代输出，返回类型为list[str]
        print(header_row)

        # 读取表头索引和内容
        for index, column_header in enumerate(header_row):
            print(str(index)+":"+column_header)

        # 读取温度和x轴日期
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows

# 文件路径
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'

# 读取温度和时间
dates1, highs1, lows1 = read_tempture(filename1)
dates2, highs2, lows2 = read_tempture(filename2)

# 创建图片
fig = plt.figure()
weather_fig1, weather_fig2 = fig.subplots(1, 2)
weather_fig1.plot(dates1, highs1, c='red', alpha=0.7) # Alpha 值为0表示完全透明， 1（默认设置） 表示完全不透明。
weather_fig1.plot(dates1, lows1, c='blue', alpha=0.7)
weather_fig2.plot(dates2, highs2, c='red', alpha=0.7)
weather_fig2.plot(dates2, lows2, c='blue', alpha=0.7)

# 设置图形格式
fig.autofmt_xdate() # 旋转日期标签
weather_fig1.set_title("Daily high and low temperatures-2014", fontsize=18)
weather_fig2.set_title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=18)
# weather_fig.tick_params(axis='both', which='major', labelsize=10)
weather_fig1.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1) # 给图表区域着色
weather_fig2.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
weather_fig1.set_ylabel("Temperature(F)", fontsize=16)
weather_fig2.set_ylabel("Temperature(F)", fontsize=16)

# 显示图片
plt.show()


"""
1.这里解释一下参数类型：Iterable[str]，它表示每次输出为字符串对象的可迭代体对象，如列表，文件等。
2.重新认识列表和字典：list是一个可以存放任意对象（如str, int, 自定义对象）的对象，同样字典中的值也可以是任意对象
"""