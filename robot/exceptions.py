class RobotError(Exception):
    pass


class NotValidXError(RobotError):
    pass


class NotValidDirectionError(RobotError):
    pass
