import pytest
from freezegun import freeze_time

from robot.schedule import Schedule


class TestSchedule:
    @pytest.mark.parametrize("rule,current_date,result", [
        ('Holiday', '2021-03-22', True),
        ('Holiday', '2021-03-23', True),
        ('Holiday', '2021-03-24', True),
        ('Holiday', '2021-03-25', True),
        ('Holiday', '2021-03-26', True),
        ('Holiday', '2021-03-27', False),
        ('Holiday', '2021-03-28', False),
        ('Workday', '2021-03-28', False),
    ])
    def test_week_day_holiday_or_not(self, rule, current_date, result):
        schedule = Schedule(rule)
        with freeze_time(current_date):
            assert schedule.validate() is result
