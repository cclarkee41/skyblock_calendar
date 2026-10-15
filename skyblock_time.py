# skyblock_time.py

import time
from datetime import datetime, timezone


SKYBLOCK_EPOCH = 1560275700

REAL_SECONDS_PER_SB_DAY = 20 * 60

SB_DAYS_PER_MONTH = 31
SB_MONTHS_PER_YEAR = 12
SB_DAYS_PER_YEAR = SB_DAYS_PER_MONTH * SB_MONTHS_PER_YEAR


MONTHS = [
    "Early Spring",
    "Spring",
    "Late Spring",
    "Early Summer",
    "Summer",
    "Late Summer",
    "Early Autumn",
    "Autumn",
    "Late Autumn",
    "Early Winter",
    "Winter",
    "Late Winter",
]


def get_skyblock_time(timestamp=None):
    if timestamp is None:
        timestamp = time.time()

    seconds_since_epoch = timestamp - SKYBLOCK_EPOCH
    total_sb_days = seconds_since_epoch / REAL_SECONDS_PER_SB_DAY

    year = int(total_sb_days // SB_DAYS_PER_YEAR) + 1

    day_of_year = int(total_sb_days % SB_DAYS_PER_YEAR)

    month_index = day_of_year // SB_DAYS_PER_MONTH
    day = day_of_year % SB_DAYS_PER_MONTH + 1

    return {
        "year": year,
        "month": MONTHS[month_index],
        "month_index": month_index,
        "day": day,
    }


def skyblock_to_real(year, month, day):
    year_offset = year - 1

    total_days = (
        year_offset * SB_DAYS_PER_YEAR
        + month * SB_DAYS_PER_MONTH
        + (day - 1)
    )

    unix_timestamp = (
        SKYBLOCK_EPOCH
        + total_days * REAL_SECONDS_PER_SB_DAY
    )

    return datetime.fromtimestamp(
        unix_timestamp,
        tz=timezone.utc,
    )


if __name__ == "__main__":
    current = get_skyblock_time()

    print(
        f"SkyBlock Year {current['year']}, "
        f"{current['month']} {current['day']}"
    )