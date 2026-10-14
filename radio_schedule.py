"""Manage and demonstrate a small radio programme schedule."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE slots ("
    "id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
    "start_hour INTEGER, minutes INTEGER)"
)
def add_slot(show, host, start_hour, minutes):
    """Add a show slot to the schedule."""
    conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a readable label for a show and its host."""
    return f"{show} hosted by {host}"


def overlap_free(start_hour, minutes, other_start_hour, other_minutes):
    """Return whether two show intervals do not overlap."""
    show_end = start_hour + minutes / 60
    other_show_end = other_start_hour + other_minutes / 60
    return show_end <= other_start_hour or other_show_end <= start_hour


def morning_shows():
    """Return the shows scheduled to start before noon."""
    return [
        row[0]
        for row in conn.execute(
            "SELECT show FROM slots WHERE start_hour < 12"
        )
    ]


def remove_slot(slot_id):
    """Remove a show slot by its ID."""
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run the radio schedule demonstration."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free(7, 60, 13, 45), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
