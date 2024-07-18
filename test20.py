# json数据

import json

#写入数据
number = [4, 5, 6, 7, 8]
file_name = 'numbers.json'
with open(file_name, 'w') as file_object:
    json.dump(number,file_object)

#加载数据
with open(file_name) as file_object_1:
    number = json.load(file_object_1)

print(number)