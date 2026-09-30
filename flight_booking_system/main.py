# Main Application Controller and Entry Point

from display import show_flights, show_classes, show_seats
from booking_engine import get_occupied_seats, book_flight, cancel_booking
from reports import show_all_bookings, search_booking, sales_report
from flight_data import get_flights

def run_action(choice):
    """Routes user choice to corresponding program module."""
    if choice == "1":
        # Book Flight Workflow
        show_flights()
        try:
            f_choice = int(input("Select Flight: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        f_list = get_flights()
        if f_choice < 1 or f_choice > len(f_list):
            print("Invalid flight selection.")
            return

        f_date = input("Enter Date (DD-MM-YYYY): ").strip()
        if not f_date:
            print("Date cannot be empty.")
            return

        selected_flight = f_list[f_choice - 1]
        key = f"{selected_flight['n']}|{f_date}"
        occupied = get_occupied_seats(key)

        if len(occupied) >= 20:
            print("Flight is fully booked for this date.")
            return

        show_classes()
        try:
            c_choice = int(input("Select Class: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        show_seats(occupied)
        try:
            seat_num = int(input("Select Seat: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        p_name = input("Enter Passenger Name: ").strip()
        if not p_name:
            print("Passenger name cannot be empty.")
            return

        book_flight(f_choice, f_date, c_choice, seat_num, p_name)

    elif choice == "2":
        # Cancel Booking Workflow
        try:
            b_id = int(input("Enter Booking ID to Cancel: "))
            cancel_booking(b_id)
        except ValueError:
            print("Invalid input. Please enter a numerical Booking ID.")

    elif choice == "3":
        # View All Bookings
        show_all_bookings()

    elif choice == "4":
        # Search Booking by ID
        try:
            b_id = int(input("Enter Booking ID to Search: "))
            search_booking(b_id)
        except ValueError:
            print("Invalid input. Please enter a numerical Booking ID.")

    elif choice == "5":
        # Sales Report
        sales_report()

    elif choice == "6":
        # Exit Application
        print("Thank you for using Flight Booking Management System!")
        return False

    else:
        print("Invalid choice. Please pick an option between 1 and 6.")

    return True

def main():
    """Main terminal loop."""
    running = True
    while running:
        print("\n===== FLIGHT BOOKING =====")
        print("1. Book Flight")
        print("2. Cancel Booking")
        print("3. Show Bookings")
        print("4. Search Booking")
        print("5. Sales Report")
        print("6. Exit")
        choice = input("Enter Choice: ").strip()
        running = run_action(choice)

if __name__ == "__main__":
    main()
  
