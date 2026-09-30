# Flight Schedules and Travel Class Data Providers

def get_flights():
    """Returns available flight routes and base pricing."""
    return [
        {"n": "AI101", "f": "Delhi", "t": "Mumbai", "m": "10:00 AM", "p": 4500},
        {"n": "AI202", "f": "Mumbai", "t": "Bangalore", "m": "2:00 PM", "p": 5000},
        {"n": "6E303", "f": "Delhi", "t": "Bangalore", "m": "5:00 PM", "p": 5500},
        {"n": "6E404", "f": "Bangalore", "t": "Chennai", "m": "8:00 PM", "p": 4000}
    ]

def get_classes():
    """Returns travel class options and additional surcharges."""
    return [
        {"n": "Economy", "e": 0},
        {"n": "Premium", "e": 1500},
        {"n": "Business", "e": 4000}
    ]
