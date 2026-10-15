# hypixel_api.py

import requests


ELECTION_URL = "https://api.hypixel.net/v2/resources/skyblock/election"


def get_election_data():
    response = requests.get(ELECTION_URL, timeout=10)
    response.raise_for_status()

    return response.json()


def get_current_mayor():
    data = get_election_data()
    mayor = data.get("mayor", {})

    return {
        "name": mayor.get("name"),
        "key": mayor.get("key"),
        "perks": mayor.get("perks", []),
    }


def has_perk(perk_name):
    mayor = get_current_mayor()

    for perk in mayor["perks"]:
        if perk.get("name") == perk_name:
            return True

    return False


if __name__ == "__main__":
    mayor = get_current_mayor()

    print("Current Mayor:", mayor["name"])

    print("\nPerks:")

    for perk in mayor["perks"]:
        print("-", perk.get("name"))