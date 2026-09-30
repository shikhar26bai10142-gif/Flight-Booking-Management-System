# Central In-Memory Storage

db = {
    "seats": {},   # Maps key ("FlightNo|Date") to set of occupied seat numbers
    "counter": 0,  # Auto-incrementing counter for unique Booking IDs
    "books": {},   # Maps Booking ID (int) to 10-element ticket tuple
    "sales": []    # List tracking prices of all active bookings
}
