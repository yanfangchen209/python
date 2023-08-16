class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number  = version_number
        self.internal_temperature = 25.0
    
    def say_hi(self):
        print("Hello, my name is " + self.name + " , ready to help!")
        
    def init_hardware(self):
        print("init hardware")
    
    def print_info(self):
        self.say_hi()
        print("version number:" + str(self.version_number))
        print("Temperature" + str(self.internal_temperature))

"""
print("test")
my_robot = Robot("R2D3", 2)
my_robot.say_hi()
my_robot.init_hardware()
my_robot.print_info()

print(my_robot.name)
"""

class RoboticArm(Robot):
    def __init__(self, name, version_number, reach):
        super().__init__(name, version_number)
        self.reach = reach
    
    
    def pick_object(self, x, y):
        print("pick object on (" + str(x) + "," + str(y) + ")")