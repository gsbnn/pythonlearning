#字典 键：值
alien_0 = {'color':'green','point':5}
print(alien_0)

#字典索引[]
new_points = alien_0['point']
print("you have get "+str(new_points)+' points.')

#增加键——值对
alien_0['x_potions'] = 0
alien_0['y_potions'] = 25
print(alien_0)

#空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#删除键——值对
del alien_0['color']
print(alien_0)

#多行字典格式
favorite_languages = {
    'jen' :'c',
    'sarah' : 'python',
    'edward' : 'java',
    'phil' : 'python',
}

#遍历字典,items()将键值对转换成元组
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
print(favorite_languages.items())

#遍历键
for name in favorite_languages.keys():
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#遍历值
for language in favorite_languages.values():
    print(language.title())

#遍历值但不重复且值无序
for language in set(favorite_languages.values()):
    print(language.title())


    