# Console Display Utilities

from .flight_data import get_flights, get_classes
def show_flights():
    """Displays available flight itineraries."""
    flist = get_flights()
    print("\n===== FLIGHTS =====")
    for idx, f in enumerate(flist, start=1):
        print(f"{idx} {f['n']} - {f['f']} to {f['t']} - {f['m']} - Rs. {f['p']}")

def show_classes():
    """Displays travel class options and extra charges."""
    clist = get_classes()
    print("\n===== CLASS =====")
    for idx, c in enumerate(clist, start=1):
        print(f"{idx} {c['n']} - Rs. {c['e']}")

def show_seats(occupiedset):
    """Renders a 4x5 visual seating map grid (20 seats total)."""
    print("\n===== SEATS =====")
    for seatnum in range(1, 21):
        if seatnum in occupiedset:
            print("[X]", end=" ")
        else:
            print(f"[{seatnum}]", end=" ")
        if seatnum % 5 == 0:
            print()
