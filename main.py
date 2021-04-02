from robot.manipulator import Manipulator
from robot.robot import RobotHod
from robot.schedule import Schedule

schedule = Schedule(rule='Holiday')
robo = RobotHod(x=0, y=0, schedule=schedule)

man = Manipulator(robot=robo, coordinate=[5, 3])
man.run()
