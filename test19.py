# 写入文件, 'w'
filename = 'programming.txt'
with open(filename, 'w') as file_object:    # 省略第二个参数,默认为只读模式打开
                                            # 找不到文件会自动创建文件
    file_object.write("hello world!\n")     # Python只能将字符串写入文本文件。 
    file_object.write("i love python\n")    # 要将数值数据存储到文本文件中， 必须先使用函数str() 将其转换为字符串格式。
                                            # 需要手动添加换行符
# 附加到文件, 'a'
with open(filename, 'a') as file_object_1:
    file_object_1.write("I also love finding meaning in large datasets.\n")
    file_object_1.write("I love creating apps that can run in a browser.\n")

# 错误异常处理
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:               # 错误输出
        print("You can't divide by 0!")     # 如果此处为Pass,出现错误时，也不会出现错误提示
    else:                                   # 正确输出
        print(answer)