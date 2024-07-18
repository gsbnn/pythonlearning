#输入函数
height = input("How tall are you, in inches? ") #输入的是字符串
height = int(height)  #将字符串转为数值
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#while循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#多个cat,注意删除
while 'cat' in pets:
    pets.remove('cat')
print(pets)