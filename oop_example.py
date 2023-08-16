from robot import Robot
from robot import RoboticArm

robot_1 = Robot("jim", 12)
robot_1_arm = RoboticArm("jim", 12, 300)

robot_1.say_hi();
robot_1_arm.pick_object(3, 4)

