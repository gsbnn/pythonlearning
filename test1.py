#修改列表值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1])
bicycles[0] = 'futiao'
print(bicycles)

#添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') #末尾添加
print(motorcycles)

#创建空列表
motorcycles = [] 
#利用append来添加元素
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#插入元素，原位置元素向右移动
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#弹出元素，并返回该元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#根据元素值删除元素，remove只能删除第一个值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
