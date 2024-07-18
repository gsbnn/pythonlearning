#列表排序
rank = [1,2,3,0]
rank.sort() #正向排序
print(rank)
rank.sort(reverse=True) #逆向排序
print(rank)

#临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

#反转列表
cars.reverse()
print(cars)

#列表长度
print(len(cars))