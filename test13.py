#创建类
class Dog(): #类
    def __init__(self, name, age): #方法（与普通函数相同）
        """初始化属性name和age"""
        self.names = name  #属性（创建的变量）
        self.ages = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.names.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.names.title() + " rolled over!")

my_dog = Dog('willie', 6) #创建实例
print(my_dog.names) #调用属性
my_dog.sit() #调用方法
my_dog.roll_over()


#指定属性的默认值
class Car():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0 #默认值为0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#修改属性的值

#直接通过实例进行修改； 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#通过方法进行设置； 
class Cars():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0 #默认值为0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

my_new_car = Cars('audi', 'a4', 2016)
my_new_car.update_odometer(200)
my_new_car.read_odometer()
