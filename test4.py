#平方函数
squares = []
for value in range(1,11):
    squares.append(value**2) # **表示乘方
print(squares)

#列表解析
squares = [value**2 for value in range(1,11,2)]
print(squares)

#列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #索引在最后第二个参数前停止
print(players[:4])
print(players[2:])
print(players[-3:])

#切片遍历
for player in players[:3]:
    print(player.title())

#切片复制
my_foods = ['pizza', 'falafel', 'carrot cake']
#全部复制 注意：friend_foods = my_foods这种写法只是把my_foods的地址赋给了friend_foods
friend_foods = my_foods[:]  
print(friend_foods)

#元组：元素不可更改
dimensions = (200, 50)
print(dimensions)
