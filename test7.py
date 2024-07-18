#将字典键值赋给列表
favorite_languages = {
    'jen' :'c',
    'sarah' : 'python',
    'edward' : 'java',
    'phil' : 'python',
}
name_list = []
language_list = []
for name,language in favorite_languages.items():
    name_list.append(name.title())
    language_list.append(language.title())
print(name_list)
print(language_list)

#字典列表

#方式一
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

#方式二，利用range()
aliens = [] #空列表
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)
for alien in aliens[:10]:
    print(alien)

#字典中存列表
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print('\t' + topping)

#字典中存字典
#用户文件夹
#有两个用户——键，对应值是用户信息
#用户信息——键值对
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
    print("\nuser's name is " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())