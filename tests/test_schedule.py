from datetime import datetime
from unittest.mock import patch

from freezegun import freeze_time

from robot.schedule import Schedule


class TestSchedule:
    def test_week_day_holiday_monday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-22'):
            assert schedule.validate() is True

    def test_week_day_holiday_tuesday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-23'):
            assert schedule.validate() is True

    def test_week_day_holiday_wednesday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-24'):
            assert schedule.validate() is True

    def test_week_day_holiday_thursday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-25'):
            assert schedule.validate() is True

    def test_week_day_holiday_friday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-26'):
            assert schedule.validate() is True

    def test_week_day_holiday_saturday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-27'):
            assert schedule.validate() is False

    def test_week_day_holiday_sanday(self):
        schedule = Schedule(rule='Holiday')
        with freeze_time('2021-03-28'):
            assert schedule.validate() is False

    def test_week_day_wrong_rule(self):
        schedule = Schedule(rule='Workday')
        assert schedule.validate() is False
