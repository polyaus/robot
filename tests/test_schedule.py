import pytest
from freezegun import freeze_time

from robot.schedule import HolidaySchedule


class TestSchedule:
    def test_schedule_object_to_str(self):
        schedule = HolidaySchedule()
        assert str(schedule) == 'HolidaySchedule()'

    @pytest.mark.parametrize("current_date,result", [
        ('2021-03-22', True),
        ('2021-03-23', True),
        ('2021-03-24', True),
        ('2021-03-25', True),
        ('2021-03-26', True),
        ('2021-03-27', False),
        ('2021-03-28', False),
        ('2021-03-28', False),
    ])
    def test_week_day_holiday_or_not(self, current_date, result):
        schedule = HolidaySchedule()
        with freeze_time(current_date):
            assert schedule.validate() is result
