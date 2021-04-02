import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Schedule:
    def __init__(self, rule):
        self.rule = rule

    def __str__(self):
        return f'Schedule(rule={self.rule})'

    def validate(self):
        if self.rule == 'Holiday':
            week_day = datetime.today().weekday()
            return week_day < 5
        return False
