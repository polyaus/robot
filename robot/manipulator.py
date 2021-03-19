from robot.robot import Directions, RobotHod


class Manipulator:
    def __init__(self, robot: RobotHod, coordinate):
        self.robot = robot
        self.coordinate = coordinate

    def run(self):
        # 5 3
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
                self.robot.turn_right()
            while y > self.robot.y:
                self.robot.go_next()
            while y < self.robot.y:
                self.robot.go_back()
