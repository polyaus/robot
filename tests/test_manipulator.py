import pytest

from robot.exceptions import NotValidRobotError, NotValidCoordinateTypeError
from robot.manipulator import Manipulator
from robot.robot import RobotHod


class TestManipulator:
    def setup_method(self, method):
        self.robo = RobotHod(0, 0)

    def test_manipulator_wrong_base_state(self):
        with pytest.raises(NotValidRobotError):
            Manipulator('robot', [0, 0])

    def test_manipulator_type_error(self):
        with pytest.raises(NotValidCoordinateTypeError):
            Manipulator(self.robo, 'az')

    def test_manipulator_type_error_for_x(self):
        with pytest.raises(NotValidCoordinateTypeError):
            Manipulator(self.robo, ['z', 0])

    def test_manipulator_type_error_for_y(self):
        with pytest.raises(NotValidCoordinateTypeError):
            Manipulator(self.robo, [0, 'k'])

    def test_manipulator_base_state(self):
        man = Manipulator(self.robo, [0, 0])
        man.run()
        assert self.robo.x == 0
        assert self.robo.y == 0

    def test_manipulator_go_to_5_9(self):
        man = Manipulator(self.robo, [5, 9])
        man.run()
        assert self.robo.x == 5
        assert self.robo.y == 9

    def test_manipulator_go_to_min3_min19(self):
        man = Manipulator(self.robo, [-3, -19])
        man.run()
        assert self.robo.x == -3
        assert self.robo.y == -19

    def test_manipulator_go_from_5_2_to_15_9(self):
        robo = RobotHod(5, 2)
        man = Manipulator(robo, [15, 9])
        man.run()
        assert robo.x == 15
        assert robo.y == 9

    def test_manipulator_go_from_5_2_to_5_9(self):
        robo = RobotHod(5, 2)
        man = Manipulator(robo, [15, 9])
        man.run()
        assert robo.x == 15
        assert robo.y == 9
