#输入字典
responses = {}
active = True
while active:
    name = input("what is your name? ")  #键
    mountain = input("Which mountain would you like to climb someday? ")  #值
    responses[name] = mountain #存入
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
for name,response in responses.items():
    print(name.title() + ":" + response.title())

#转移字典
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:   #字典非空
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)