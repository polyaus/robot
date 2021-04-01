from robot.exceptions import NotValidRobotError, NotValidCoordinateTypeError
from robot.robot import Directions, RobotHod


class Manipulator:
    def __init__(self, robot: RobotHod, coordinate):
        if not isinstance(robot, RobotHod):
            raise NotValidRobotError('Robot can be only RobotHod!')

        if not isinstance(coordinate, list):
            raise NotValidCoordinateTypeError()

        if not isinstance(coordinate[0], int) or not isinstance(coordinate[1], int):
            raise NotValidCoordinateTypeError()

        self.robot = robot
        self.coordinate = coordinate

    def run(self):
        x = self.coordinate[0]
        y = self.coordinate[1]
        if x != self.robot.x:
            while self.robot.direction != Directions.RIGHT.value:
                self.robot.turn_right()
            while x > self.robot.x:
                self.robot.go_next()
            while x < self.robot.x:
                self.robot.go_back()
        if y != self.robot.y:
            while self.robot.direction != Directions.UP.value:
                self.robot.turn_left()
            while y > self.robot.y:
                self.robot.go_next()
            while y < self.robot.y:
                self.robot.go_back()
