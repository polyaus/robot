import enum

from robot.exceptions import NotValidXError, NotValidDirectionError


@enum.unique
class Directions(enum.Enum):
    UP = 'up'
    RIGHT = 'right'
    LEFT = 'left'
    DOWN = 'down'


class RobotHod:
    def __init__(self, x, y, schedule=None):
        if not isinstance(x, int) or not isinstance(y, int):
            raise NotValidXError()

        self.x = x
        self.y = y
        self.direction = Directions.UP.value
        self.schedule = schedule

    def turn_right(self):
        if self.direction == Directions.UP.value:
            self.direction = Directions.RIGHT.value
        elif self.direction == Directions.RIGHT.value:
            self.direction = Directions.DOWN.value
        elif self.direction == Directions.DOWN.value:
            self.direction = Directions.LEFT.value
        elif self.direction == Directions.LEFT.value:
            self.direction = Directions.UP.value
        else:
            raise NotValidDirectionError()

    def turn_left(self):
        if self.direction == Directions.UP.value:
            self.direction = Directions.LEFT.value
        elif self.direction == Directions.LEFT.value:
            self.direction = Directions.DOWN.value
        elif self.direction == Directions.DOWN.value:
            self.direction = Directions.RIGHT.value
        elif self.direction == Directions.RIGHT.value:
            self.direction = Directions.UP.value
        else:
            raise NotValidDirectionError()

    def go_next(self):
        if self.direction == Directions.UP.value:
            self.y += 1
        elif self.direction == Directions.LEFT.value:
            self.x -= 1
        elif self.direction == Directions.DOWN.value:
            self.y -= 1
        elif self.direction == Directions.RIGHT.value:
            self.x += 1
        else:
            raise NotValidDirectionError()

    def go_back(self):
        if self.direction == Directions.UP.value:
            self.y -= 1
        elif self.direction == Directions.LEFT.value:
            self.x += 1
        elif self.direction == Directions.DOWN.value:
            self.y += 1
        elif self.direction == Directions.RIGHT.value:
            self.x -= 1
        else:
            raise NotValidDirectionError()
