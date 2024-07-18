#向函数传递列表（或字典等复杂数据类型）
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计， 直到没有未打印的设计为止

    打印每个设计后， 都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_design,completed_models)
print(completed_models)
print(unprinted_design)

#禁止在函数中修改列表
#向函数传递列表副本——list[:]
unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_design[:], completed_models)
print(completed_models)
print(unprinted_design)

#传递任意数量的实参
def make_pizza(*toppings):
    """
    打印顾客点的所有配料

    形参名*toppings 中的星号让Python创建一个名为toppings 的空元组， 并将收到的所有值都封装到这个元组中。 
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

#如果要让函数接受不同类型的实参， 必须在函数定义中将接纳任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#传递任意数量的关键字实参
#以键-值对方式传送
def build_profile(first, last, **user_info):
    '''
    形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典

    并将收到的所有名称—值对都封装到这个字典中
    '''
    profile = {} #空字典
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
