from datetime import datetime


class Schedule:
    def __init__(self, rule):
        self.rule = rule

    def validate(self):
        if self.rule == 'Holiday':
            week_day = datetime.today().weekday()
            return week_day < 5
        return False
