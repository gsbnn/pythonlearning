#for 循环输出列表,同级缩进表示同一层
magicians = ['alice', 'david', 'carolina']
for magican in magicians:
    print(magican)
    print(magican.title()+" "+"is wonderful!\r\n")
print("fuck you!")


#使用range()生成数值列表

#range(1,5)表示从第一元素开始，到第五个元素结束，但不包括最后一个元素
for value in range(1,5):
    print(value)

#将序列转换成列表 list()
nums = list(range(1,5))
print(nums)

#range()第三个参数为步长
nums = list(range(1,11,2))
print(nums)

#寻找最小值，最大值，求和
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))