#创建子类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        """super() 是一个特殊函数， 帮助Python将父类和子类关联起来"""
        self.battery_size = 70  #子类的属性
    
    def describe_battery(self): #子类的方法
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.read_odometer() #继承父类的方法
my_tesla.describe_battery()

#重写父类方法
"""
对于父类的方法， 只要它不符合子类模拟的实物的行为， 都可对其进行重写。 
为此， 可在子类中定义一个这样的方法， 即它与要重写的父类方法同名。
这样， Python将不会考虑这个父类方法， 而只关注你在子类中定义的相应方法。

假设Car 类有一个名为fill_gas_tank() 的方法， 它对全电动汽车来说毫无意义， 因此你可能想重写它。 下面演示了一种重写方式

def ElectricCar(Car):
    --snip--
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

现在， 如果有人对电动汽车调用方法fill_gas_tank() ， Python将忽略Car 类中的方法fill_gas_tank() ， 转而运行上述代码。 
"""
