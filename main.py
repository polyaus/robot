from robot.manipulator import Manipulator
from robot.robot import RobotHod

robo = RobotHod(0, 0)
print(robo.x, robo.y)
man = Manipulator(robo, [5, 3])
man.run()
print(robo.x, robo.y)
