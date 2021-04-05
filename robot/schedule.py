import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class HolidaySchedule:
    def __str__(self):
        return 'HolidaySchedule()'

    @staticmethod
    def validate():
        week_day = datetime.today().weekday()
        return week_day < 5
