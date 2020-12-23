from datetime import datetime

from src.date_textualizer.date2text import date2text
from src.date_textualizer.time2text import time2absolutetexttime, time2digi, time2relitivetexttime


class DatetimeTextualizer:

    def __init__(self, now: datetime = datetime.now()):
        self.now = now

    def generate_candidates(self, datetime: datetime, time_precision: int = 3):
        dates = [date2text(datetime.date(), self.now.date())]
        times = [time2absolutetexttime(datetime.time(), time_precision),
                 time2digi(datetime.time(), time_precision),
                 time2relitivetexttime(datetime.time(), time_precision)]

        return {
            "date": dates,
            "times": times
        }


if __name__ == '__main__':
    dt = DatetimeTextualizer()

    print(dt.generate_candidates(datetime(2021, 12, 30)))