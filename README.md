# Flight Booking Management System

A modular, terminal-based Python application for managing flight schedules, visual seat maps, ticket reservations, cancellations, customer searches, and sales analytics[cite: 1, 2]. Built using pure Python without external dependencies or database drivers.

## Repository Structure

```text
flight_booking_system/
│
├── main.py                   # Main application entry point & menu loop
├── database.py               # In-memory data store (db)
├── flight_data.py            # Flight itineraries and travel class surcharges
├── display.py                # Console rendering for schedules, classes, and seat grid
├── booking_engine.py         # Core business logic for booking, canceling, and ID generation
├── reports.py                # Search utilities and financial summary calculations
├── README.md                 # Project overview and setup instructions
└── statement.md              # Project statement and requirements breakdown
