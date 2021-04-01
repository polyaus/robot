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

    @pytest.mark.parametrize('coordinate', [
        ('az',),
        (['z', 0],),
        ([0, 'k'],),
    ])
    def test_manipulator_type_error(self, coordinate):
        with pytest.raises(NotValidCoordinateTypeError):
            Manipulator(self.robo, coordinate)

    @pytest.mark.parametrize('coordinates,result_x,result_y', [
        ([0, 0], 0, 0,),
        ([5, 9], 5, 9,),
        ([-3, -19], -3, -19,),
    ])
    def test_manipulator_change_coordinates(self, coordinates, result_x, result_y):
        Manipulator(self.robo, coordinates).run()
        assert self.robo.x == result_x
        assert self.robo.y == result_y

    @pytest.mark.parametrize('point_robo_x,point_robo_y,points_manipulator,final_x,final_y', [
        (5, 2, [15, 9], 15, 9,),
        (5, 2, [5, 9], 5, 9,),
    ])
    def test_manipulator_go_from_5_2_to_15_9(self, point_robo_x, point_robo_y, points_manipulator, final_x, final_y):
        robo = RobotHod(point_robo_x, point_robo_y)
        Manipulator(robo, points_manipulator).run()
        assert robo.x == final_x
        assert robo.y == final_y

    def test_manipulator_go_from_0_0_to_5_3_run_turn_right_turn_left(self, mocker):
        robo = RobotHod(0, 0)
        man = Manipulator(robo, [5, 3])

        spy_right = mocker.spy(robo, 'turn_right')
        spy_left = mocker.spy(robo, 'turn_left')
        man.run()
        spy_right.assert_has_calls([mocker.call()])
        spy_left.assert_has_calls([mocker.call()])
