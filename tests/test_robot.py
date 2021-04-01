from unittest.mock import patch

import pytest
from freezegun import freeze_time

from robot.exceptions import NotValidXError, NotValidDirectionError, RobotOffError, NotValidYError
from robot.robot import RobotHod, Directions
from robot.schedule import Schedule


class TestRobot:
    def setup_method(self, method):
        self.robo = RobotHod(0, 0)

    def test_robot_base_state(self):
        assert self.robo.x == 0
        assert self.robo.y == 0
        assert self.robo.direction == Directions.UP.value

    @pytest.mark.parametrize("turn_count,direction", [
        (1, Directions.RIGHT.value),
        (2, Directions.DOWN.value),
        (3, Directions.LEFT.value),
        (4, Directions.UP.value),
    ])
    def test_robot_turn_right(self, turn_count, direction):
        for _ in range(turn_count):
            self.robo.turn_right()
        assert self.robo.direction == direction

    @pytest.mark.parametrize("turn_count,direction", [
        (1, Directions.LEFT.value),
        (2, Directions.DOWN.value),
        (3, Directions.RIGHT.value),
        (4, Directions.UP.value),
    ])
    def test_robot_turn_left(self, turn_count, direction):
        for _ in range(turn_count):
            self.robo.turn_left()
        assert self.robo.direction == direction

    @pytest.mark.parametrize('method,x,y', [
        ('go_next', 0, 1),
        ('go_back', 0, -1),
    ])
    def test_robot_go_and_check_x_y(self, method, x, y):
        getattr(self.robo, method)()
        assert self.robo.x == x
        assert self.robo.y == y

    @pytest.mark.parametrize('turn_count,method,turn_count_2,method_2,direction,x,y', [
        (2, 'turn_right', 1, 'go_next', Directions.DOWN.value, 0, -1),
        (3, 'turn_right', 1, 'go_next', Directions.LEFT.value, -1, 0),
        (1, 'turn_left', 2, 'go_back', Directions.LEFT.value, 2, 0),
        (2, 'turn_left', 1, 'go_back', Directions.DOWN.value, 0, 1),
    ])
    def test_robot_mix_actions(self, turn_count, method, turn_count_2, method_2, direction, x, y):
        for _ in range(turn_count):
            getattr(self.robo, method)()
        for _ in range(turn_count_2):
            getattr(self.robo, method_2)()
        assert self.robo.direction == direction
        assert self.robo.x == x
        assert self.robo.y == y

    def test_robot_turn_right_twice_and_go_next_and_turn_left_and_go_back_twice(self):
        self.robo.turn_right()
        self.robo.turn_right()
        self.robo.go_next()
        assert self.robo.direction == Directions.DOWN.value
        assert self.robo.x == 0
        assert self.robo.y == -1

        self.robo.turn_left()
        self.robo.go_back()
        self.robo.go_back()
        assert self.robo.direction == Directions.RIGHT.value
        assert self.robo.x == -2
        assert self.robo.y == -1

    @pytest.mark.parametrize('x,y', [
        ('g', 0,),
        (0, 'g',),
    ])
    def test_robot_wrong_x_and_y(self, x, y):
        with pytest.raises(NotValidXError):
            RobotHod(x, y)

    @pytest.mark.parametrize('method', [
        'turn_right',
        'turn_left',
        'go_next',
        'go_back',
    ])
    def test_robot_turn_right_wrong_direction(self, method):
        with pytest.raises(NotValidDirectionError):
            with patch.object(self.robo, 'direction', new='error'):
                getattr(self.robo, method)()

    def test_robot_on(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-26'):
            with patch.object(self.robo, 'schedule', new=schedule):
                self.robo.turn_right()
                self.robo.turn_left()
                self.robo.go_next()
                self.robo.go_back()
        assert self.robo.x == 0
        assert self.robo.y == 0

    @pytest.mark.parametrize('method', [
        'turn_right',
        'turn_left',
        'go_next',
        'go_back',
    ])
    def test_robot_off(self, method):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-27'):
            with patch.object(self.robo, 'schedule', new=schedule):
                with pytest.raises(RobotOffError):
                    getattr(self.robo, method)()
        assert self.robo.x == 0
        assert self.robo.y == 0
