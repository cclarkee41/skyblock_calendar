# calendar_export.py

from icalendar import Calendar, Event


def create_ics(events):
    calendar = Calendar()

    calendar.add(
        "prodid",
        "-//Hypixel SkyBlock Calendar//"
    )

    calendar.add(
        "version",
        "2.0"
    )

    for item in events:
        event = Event()

        event.add(
            "summary",
            item["name"]
        )

        event.add(
            "dtstart",
            item["start"]
        )

        event.add(
            "dtend",
            item["end"]
        )

        event.add(
            "description",
            f"SkyBlock Year {item['skyblock_year']}"
        )

        calendar.add_component(event)

    return calendar


def save_calendar(events, filename="skyblock.ics"):
    calendar = create_ics(events)

    with open(filename, "wb") as file:
        file.write(calendar.to_ical())


if __name__ == "__main__":
    from calendar import get_upcoming_events

    events = get_upcoming_events(30)

    save_calendar(events)

    print("Created skyblock.ics")