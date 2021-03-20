import pytest

from robot.exceptions import NotValidXError, NotValidDirectionError
from robot.robot import RobotHod, Directions


def test_robot_base_state():
    robo = RobotHod(0, 0)
    assert robo.x == 0
    assert robo.y == 0
    assert robo.direction == Directions.UP.value


def test_robot_turn_right():
    robo = RobotHod(0, 0)
    robo.turn_right()
    assert robo.direction == Directions.RIGHT.value


def test_robot_turn_right_twice():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    assert robo.direction == Directions.DOWN.value


def test_robot_turn_right_third():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    robo.turn_right()
    assert robo.direction == Directions.LEFT.value


def test_robot_turn_right_four():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    robo.turn_right()
    robo.turn_right()
    assert robo.direction == Directions.UP.value


def test_robot_turn_left():
    robo = RobotHod(0, 0)
    robo.turn_left()
    assert robo.direction == Directions.LEFT.value


def test_robot_turn_left_twice():
    robo = RobotHod(0, 0)
    robo.turn_left()
    robo.turn_left()
    assert robo.direction == Directions.DOWN.value


def test_robot_turn_left_third():
    robo = RobotHod(0, 0)
    robo.turn_left()
    robo.turn_left()
    robo.turn_left()
    assert robo.direction == Directions.RIGHT.value


def test_robot_turn_left_four():
    robo = RobotHod(0, 0)
    robo.turn_left()
    robo.turn_left()
    robo.turn_left()
    robo.turn_left()
    assert robo.direction == Directions.UP.value


def test_robot_go_next():
    robo = RobotHod(0, 0)
    robo.go_next()
    assert robo.x == 0
    assert robo.y == 1


def test_robot_go_back():
    robo = RobotHod(0, 0)
    robo.go_back()
    assert robo.x == 0
    assert robo.y == -1


def test_robot_turn_right_twice_and_go_next():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    robo.go_next()
    assert robo.direction == Directions.DOWN.value
    assert robo.y == -1
    assert robo.x == 0


def test_robot_turn_right_third_and_go_next():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    robo.turn_right()
    robo.go_next()
    assert robo.direction == Directions.LEFT.value
    assert robo.x == -1
    assert robo.y == 0


def test_robot_turn_left_and_go_back_twice():
    robo = RobotHod(0, 0)
    robo.turn_left()
    robo.go_back()
    robo.go_back()
    assert robo.direction == Directions.LEFT.value
    assert robo.x == 2
    assert robo.y == 0


def test_robot_turn_left_twice_and_go_back():
    robo = RobotHod(0, 0)
    robo.turn_left()
    robo.turn_left()
    robo.go_back()
    assert robo.direction == Directions.DOWN.value
    assert robo.x == 0
    assert robo.y == 1


def test_robot_turn_right_twice_and_go_next_and_turn_left_and_go_back_twice():
    robo = RobotHod(0, 0)
    robo.turn_right()
    robo.turn_right()
    robo.go_next()
    assert robo.direction == Directions.DOWN.value
    assert robo.x == 0
    assert robo.y == -1

    robo.turn_left()
    robo.go_back()
    robo.go_back()
    assert robo.direction == Directions.RIGHT.value
    assert robo.x == -2
    assert robo.y == -1


def test_robot_wrong_x():
    with pytest.raises(NotValidXError):
        robo = RobotHod('g', 0)


def test_robot_wrong_y():
    with pytest.raises(NotValidXError):
        robo = RobotHod(0, 'g')


def test_robot_turn_right_wrong_direction():
    robo = RobotHod(0, 0)
    robo.direction = 'error'
    with pytest.raises(NotValidDirectionError):
        robo.turn_right()


def test_robot_turn_left_wrong_direction():
    robo = RobotHod(0, 0)
    robo.direction = 'error'
    with pytest.raises(NotValidDirectionError):
        robo.turn_left()


def test_robot_go_next_wrong_direction():
    robo = RobotHod(0, 0)
    robo.direction = 'error'
    with pytest.raises(NotValidDirectionError):
        robo.go_next()


def test_robot_go_back_wrong_direction():
    robo = RobotHod(0, 0)
    robo.direction = 'error'
    with pytest.raises(NotValidDirectionError):
        robo.go_back()
