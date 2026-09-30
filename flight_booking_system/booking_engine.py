# Core Reservation and Cancellation Engine

from .database import db
from .flight_data import get_flights, get_classes
def get_occupied_seats(key):
    """Retrieves or creates the occupied seat set for a flight-date key."""
    if key not in db["seats"]:
        db["seats"][key] = set()
    return db["seats"][key]

def book_flight(flight_idx, flight_date, class_idx, seat_num, passenger_name):
    """Processes flight booking, generates unique ID, and records ticket."""
    flist = get_flights()
    clist = get_classes()

    # Input validation checks
    if flight_idx < 1 or flight_idx > len(flist):
        print("Invalid flight selection.")
        return False
    if class_idx < 1 or class_idx > len(clist):
        print("Invalid class selection.")
        return False
    if seat_num < 1 or seat_num > 20:
        print("Invalid seat number. Please choose between 1 and 20.")
        return False

    flight = flist[flight_idx - 1]
    travel_class = clist[class_idx - 1]
    key = f"{flight['n']}|{flight_date}"
    occupied = get_occupied_seats(key)

    if len(occupied) >= 20:
        print("Flight is fully booked for this date.")
        return False

    if seat_num in occupied:
        print("Seat already booked. Please pick another seat.")
        return False

    # Perform reservation updates
    occupied.add(seat_num)
    db["counter"] += 1
    booking_id = db["counter"]
    total_price = flight["p"] + travel_class["e"]

    # Tuple structure: (id, name, flight_no, origin, dest, date, time, class, seat, price)
    ticket_tuple = (
        booking_id,
        passenger_name,
        flight["n"],
        flight["f"],
        flight["t"],
        flight_date,
        flight["m"],
        travel_class["n"],
        seat_num,
        total_price
    )

    db["books"][booking_id] = ticket_tuple
    db["sales"].append(total_price)

    # Print receipt
    print("\n===== BOOKING CONFIRMED =====")
    print(f"ID: {booking_id}")
    print(f"Name: {passenger_name}")
    print(f"Flight: {flight['n']}")
    print(f"Route: {flight['f']} to {flight['t']}")
    print(f"Date: {flight_date}")
    print(f"Time: {flight['m']}")
    print(f"Class: {travel_class['n']}")
    print(f"Seat: {seat_num}")
    print(f"Price: Rs. {total_price}")
    return True

def cancel_booking(booking_id):
    """Cancels a booking by ID, releases seat, and updates revenue logs."""
    if booking_id not in db["books"]:
        print("Booking ID not found.")
        return False

    ticket = db["books"][booking_id]
    flight_no = ticket[2]
    flight_date = ticket[5]
    seat_num = ticket[8]
    price = ticket[9]

    key = f"{flight_no}|{flight_date}"

    # Release occupied seat
    if key in db["seats"] and seat_num in db["seats"][key]:
        db["seats"][key].remove(seat_num)

    # Remove reservation record and deduct sale
    del db["books"][booking_id]
    if price in db["sales"]:
        db["sales"].remove(price)

    print(f"Booking ID {booking_id} successfully cancelled.")
    return True
