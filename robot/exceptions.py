class RobotError(Exception):
    pass


class RobotOffError(RobotError):
    pass


class NotValidXError(RobotError):
    pass


class NotValidYError(RobotError):
    pass


class NotValidDirectionError(RobotError):
    pass


class ManipulatorError(Exception):
    pass


class NotValidRobotError(ManipulatorError):
    pass


class NotValidCoordinateError(ManipulatorError):
    pass


class NotValidCoordinateTypeError(NotValidCoordinateError):
    pass
