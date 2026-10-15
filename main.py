# main.py

from flask import Flask, Response

from calendar import get_upcoming_events
from calendar_export import create_ics


app = Flask(__name__)


@app.route("/")
def home():
    return "Hypixel SkyBlock Calendar is running."


@app.route("/skyblock.ics")
def skyblock_calendar():
    events = get_upcoming_events(60)

    calendar_data = create_ics(events)

    return Response(
        calendar_data.to_ical(),
        mimetype="text/calendar",
        headers={
            "Content-Disposition": "inline; filename=skyblock.ics"
        },
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=500,
        debug=True,
    )