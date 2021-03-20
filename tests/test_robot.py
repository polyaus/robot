import pytest

from robot.exceptions import NotValidXError, NotValidDirectionError
from robot.robot import RobotHod, Directions


class TestRobot:
    def setup_method(self, method):
        self.robo = RobotHod(0, 0)

    def test_robot_base_state(self):
        assert self.robo.x == 0
        assert self.robo.y == 0
        assert self.robo.direction == Directions.UP.value

    def test_robot_turn_right(self):
        self.robo.turn_right()
        assert self.robo.direction == Directions.RIGHT.value

    def test_robot_turn_right_twice(self):
        self.robo.turn_right()
        self.robo.turn_right()
        assert self.robo.direction == Directions.DOWN.value

    def test_robot_turn_right_third(self):
        for _ in range(3):
            self.robo.turn_right()
        assert self.robo.direction == Directions.LEFT.value

    def test_robot_turn_right_four(self):
        for _ in range(4):
            self.robo.turn_right()
        assert self.robo.direction == Directions.UP.value

    def test_robot_turn_left(self):
        self.robo.turn_left()
        assert self.robo.direction == Directions.LEFT.value

    def test_robot_turn_left_twice(self):
        self.robo.turn_left()
        self.robo.turn_left()
        assert self.robo.direction == Directions.DOWN.value

    def test_robot_turn_left_third(self):
        for _ in range(3):
            self.robo.turn_left()
        assert self.robo.direction == Directions.RIGHT.value

    def test_robot_turn_left_four(self):
        for _ in range(4):
            self.robo.turn_left()
        assert self.robo.direction == Directions.UP.value

    def test_robot_go_next(self):
        self.robo.go_next()
        assert self.robo.x == 0
        assert self.robo.y == 1

    def test_robot_go_back(self):
        self.robo.go_back()
        assert self.robo.x == 0
        assert self.robo.y == -1

    def test_robot_turn_right_twice_and_go_next(self):
        self.robo.turn_right()
        self.robo.turn_right()
        self.robo.go_next()
        assert self.robo.direction == Directions.DOWN.value
        assert self.robo.y == -1
        assert self.robo.x == 0

    def test_robot_turn_right_third_and_go_next(self):
        for _ in range(3):
            self.robo.turn_right()
        self.robo.go_next()
        assert self.robo.direction == Directions.LEFT.value
        assert self.robo.x == -1
        assert self.robo.y == 0

    def test_robot_turn_left_and_go_back_twice(self):
        self.robo.turn_left()
        self.robo.go_back()
        self.robo.go_back()
        assert self.robo.direction == Directions.LEFT.value
        assert self.robo.x == 2
        assert self.robo.y == 0

    def test_robot_turn_left_twice_and_go_back(self):
        self.robo.turn_left()
        self.robo.turn_left()
        self.robo.go_back()
        assert self.robo.direction == Directions.DOWN.value
        assert self.robo.x == 0
        assert self.robo.y == 1

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

    def test_robot_wrong_x(self):
        with pytest.raises(NotValidXError):
            RobotHod('g', 0)

    def test_robot_wrong_y(self):
        with pytest.raises(NotValidXError):
            RobotHod(0, 'g')

    def test_robot_turn_right_wrong_direction(self):
        self.robo.direction = 'error'
        with pytest.raises(NotValidDirectionError):
            self.robo.turn_right()

    def test_robot_turn_left_wrong_direction(self):
        self.robo.direction = 'error'
        with pytest.raises(NotValidDirectionError):
            self.robo.turn_left()

    def test_robot_go_next_wrong_direction(self):
        self.robo.direction = 'error'
        with pytest.raises(NotValidDirectionError):
            self.robo.go_next()

    def test_robot_go_back_wrong_direction(self):
        self.robo.direction = 'error'
        with pytest.raises(NotValidDirectionError):
            self.robo.go_back()
