#条件语句
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print('get out!')

#if和for配合使用
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == requested_toppings[1]:
        print("we are out of "+requested_toppings[1]+' right now!')
    else:
        print('ok!')

#循环前先检测列表是否为空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('add '+requested_topping+'.')
else:
    print('are you sure want to a pizza')



#比较两组
available_toppings = ('mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("we do not have A "+requested_topping+".")
