import enum
import logging

from robot.exceptions import NotValidXError, NotValidDirectionError, RobotOffError, NotValidYError

logger = logging.getLogger(__name__)


@enum.unique
class Directions(enum.Enum):
    UP = 'up'
    RIGHT = 'right'
    LEFT = 'left'
    DOWN = 'down'


class RobotHod:
    def __init__(self, x, y, schedule=None):
        if not isinstance(x, int):
            raise NotValidXError()
        if not isinstance(y, int):
            raise NotValidYError()

        self.x = x
        self.y = y
        self.direction = Directions.UP.value
        self.schedule = schedule

        logger.info('RobotHod init with x=%s, y=%s, direction=%s, schedule=%s', x, y, self.direction, schedule)

    def __str__(self):
        return f'RobotHod(x={self.x}, y={self.y}, schedule={self.schedule})'

    def turn_right(self):
        if self.schedule is not None and not self.schedule.validate():
            raise RobotOffError()

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

        logger.info('RobotHod turn_right new direction=%s', self.direction)

    def turn_left(self):
        if self.schedule is not None and not self.schedule.validate():
            raise RobotOffError()

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

        logger.info('RobotHod turn_left new direction=%s', self.direction)

    def go_next(self):
        if self.schedule is not None and not self.schedule.validate():
            raise RobotOffError()

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

        logger.info('RobotHod go_next new x=%s. new y=%s', self.x, self.y)

    def go_back(self):
        if self.schedule is not None and not self.schedule.validate():
            raise RobotOffError()

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

        logger.info('RobotHod go_back new x=%s. new y=%s', self.x, self.y)
