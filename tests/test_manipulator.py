from robot.manipulator import Manipulator
from robot.robot import RobotHod


def test_manipulator_base_state():
    robo = RobotHod(0, 0)
    man = Manipulator(robo, [0, 0])
    man.run()
    assert robo.x == 0
    assert robo.y == 0


def test_manipulator_go_to_5_9():
    robo = RobotHod(0, 0)
    man = Manipulator(robo, [5, 9])
    man.run()
    assert robo.x == 5
    assert robo.y == 9


def test_manipulator_go_to_min3_min19():
    robo = RobotHod(0, 0)
    man = Manipulator(robo, [-3, -19])
    man.run()
    assert robo.x == -3
    assert robo.y == -19


def test_manipulator_go_from_5_2_to_15_9():
    robo = RobotHod(5, 2)
    man = Manipulator(robo, [15, 9])
    man.run()
    assert robo.x == 15
    assert robo.y == 9

