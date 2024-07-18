#定义函数,无参数
def greet_user():
    '''函数功能：打招呼'''
    print("Hello world!")

greet_user()

#位置实参——顺序不能乱
def descirbe_pet1(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

descirbe_pet1('dog','Spike')

#关键字实参——顺序可以乱
def describe_pet2(animal_type, pet_name):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(animal_type='hamster', pet_name='harry')

#默认值——给形参一个默认实参,当未指定实参时，使用默认值
def describe_pet3(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet3(pet_name='willie') #关键字实参
describe_pet3('willie') #位置实参

#返回值
def get_formatted_name1(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name1('jimi', 'hendrix')
print(musician)

#返回多个值
def multiple_return():
    a = 1
    b = 2
    c = 3
    return a, b, c

x, y, z = multiple_return()
print(x, y, z)


#让实参变成可选的
#对于可选实参，在函数中判断其是否为空
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name #不为空，三个参数拼接
    else:
        full_name = first_name + ' ' + last_name #为空，两个个参数拼接
    return full_name

musician = get_formatted_name1('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#函数可返回任何类型的值， 包括列表和字典等较复杂的数据结构
#返回字典
def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name , 'last' : last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

