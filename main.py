from robot.manipulator import Manipulator
from robot.robot import RobotHod
from robot.schedule import Schedule

schedule = Schedule(rule='Holiday')
robo = RobotHod(0, 0, schedule)
print(robo.x, robo.y)
man = Manipulator(robo, [5, 3])
man.run()
print(robo.x, robo.y)
