# Querying and Sales Analytics Functions

from database import db

def display_booking(b):
    """Formats and prints an individual booking tuple."""
    print(f"ID: {b[0]} | Name: {b[1]} | Flight: {b[2]} ({b[3]}->{b[4]}) | Date: {b[5]} {b[6]} | Class: {b[7]} | Seat: {b[8]} | Price: Rs. {b[9]}")

def show_all_bookings():
    """Prints all active passenger records."""
    if not db["books"]:
        print("\nNo bookings found.")
        return
    print("\n===== ALL BOOKINGS =====")
    for booking_id in sorted(db["books"].keys()):
        display_booking(db["books"][booking_id])

def search_booking(booking_id):
    """Searches and prints details for a single booking ID."""
    if booking_id in db["books"]:
        print("\n===== BOOKING DETAILS =====")
        display_booking(db["books"][booking_id])
    else:
        print("Booking not found.")

def sales_report():
    """Computes and prints financial performance analytics."""
    sales = db["sales"]
    print("\n===== SALES REPORT =====")
    print(f"Bookings: {len(sales)}")
    if not sales:
        print("Revenue: Rs. 0")
        print("Highest: Rs. 0")
        print("Lowest: Rs. 0")
    else:
        total_revenue = sum(sales)
        highest_sale = max(sales)
        lowest_sale = min(sales)
        print(f"Revenue: Rs. {total_revenue}")
        print(f"Highest: Rs. {highest_sale}")
        print(f"Lowest: Rs. {lowest_sale}")
