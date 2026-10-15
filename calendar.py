# calendar.py

from datetime import datetime, timedelta, timezone

from events import EVENTS
from skyblock_time import get_skyblock_time, skyblock_to_real


def get_events_for_year(year):
    results = []

    for event in EVENTS:
        start = skyblock_to_real(
            year,
            event["month"],
            event["day"],
        )

        end = start + timedelta(
            minutes=event["duration_minutes"]
        )

        results.append(
            {
                "name": event["name"],
                "start": start,
                "end": end,
                "skyblock_year": year,
            }
        )

    return results


def get_upcoming_events(days=30):
    now = datetime.now(timezone.utc)
    end_date = now + timedelta(days=days)

    current_sb_time = get_skyblock_time()
    current_year = current_sb_time["year"]

    results = []

    for year in range(current_year, current_year + 3):
        yearly_events = get_events_for_year(year)

        for event in yearly_events:
            if now <= event["start"] <= end_date:
                results.append(event)

    return sorted(
        results,
        key=lambda event: event["start"],
    )


if __name__ == "__main__":
    events = get_upcoming_events(30)

    for event in events:
        print(
            event["start"],
            "-",
            event["name"],
        )