"""
main.py

Driver program for the Bicycle Rental System. Demonstrates the functionality
of the Bicycle class, including successful and unsuccessful operations.

Author:Muhammad Usman Waqar
"""

from bicycle import Bicycle


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    print_section("BICYCLE RENTAL SYSTEM - DEMONSTRATION")

    # ------------------------------------------------------------------
    # Create at least four bicycle objects using different methods
    # ------------------------------------------------------------------
    print_section("1. Creating Bicycles")

    bike1 = Bicycle("B001", "Mountain Pro", 5.50)
    bike2 = Bicycle("B002", "City Cruiser", 4.00)
    bike3 = Bicycle.from_string("B003, Road Racer, 7.25")
    bike4 = Bicycle.create_new("Electric Glide", 9.00)

    bicycles = [bike1, bike2, bike3, bike4]
    for bike in bicycles:
        print(f"  {bike}")

    # ------------------------------------------------------------------
    # Successful borrow
    # ------------------------------------------------------------------
    print_section("2. Successful Borrow")

    try:
        print(f"  Borrowing {bike1.bicycle_id}...")
        bike1.borrow()
        print(f"  Success: {bike1.get_description()}")
    except RuntimeError as exc:
        print(f"  Error: {exc}")

    # ------------------------------------------------------------------
    # Unsuccessful borrow (already borrowed)
    # ------------------------------------------------------------------
    print_section("3. Unsuccessful Borrow (already borrowed)")

    try:
        print(f"  Attempting to borrow {bike1.bicycle_id} again...")
        bike1.borrow()
    except RuntimeError as exc:
        print(f"  Expected error: {exc}")

    # ------------------------------------------------------------------
    # Successful return
    # ------------------------------------------------------------------
    print_section("4. Successful Return")

    try:
        print(f"  Returning {bike1.bicycle_id}...")
        bike1.return_bicycle()
        print(f"  Success: {bike1.get_description()}")
    except RuntimeError as exc:
        print(f"  Error: {exc}")

    # ------------------------------------------------------------------
    # Unsuccessful return (not borrowed)
    # ------------------------------------------------------------------
    print_section("5. Unsuccessful Return (not borrowed)")

    try:
        print(f"  Attempting to return {bike2.bicycle_id}...")
        bike2.return_bicycle()
    except RuntimeError as exc:
        print(f"  Expected error: {exc}")

    # ------------------------------------------------------------------
    # Rental cost calculation
    # ------------------------------------------------------------------
    print_section("6. Rental Cost Calculations")

    for bike in bicycles:
        cost = bike.calculate_rental_cost(3)
        print(f"  {bike.bicycle_id}: 3 hours = £{cost:.2f}")

    # ------------------------------------------------------------------
    # Price update
    # ------------------------------------------------------------------
    print_section("7. Updating a Price")

    print(f"  Old rate for {bike2.bicycle_id}: £{bike2.hourly_rate:.2f}/hour")
    bike2.update_price(4.75)
    print(f"  New rate for {bike2.bicycle_id}: £{bike2.hourly_rate:.2f}/hour")

    # ------------------------------------------------------------------
    # Invalid operations (exception handling demonstration)
    # ------------------------------------------------------------------
    print_section("8. Invalid Operations")

    invalid_cases = [
        ("Negative hourly rate", lambda: Bicycle("B999", "Bad Bike", -5)),
        ("Empty model name", lambda: Bicycle("B998", "", 5)),
        ("Zero hourly rate", lambda: Bicycle("B997", "Zero Bike", 0)),
        ("Negative rental hours", lambda: bike2.calculate_rental_cost(-2)),
        ("Bad data string", lambda: Bicycle.from_string("not,enough")),
    ]

    for label, operation in invalid_cases:
        try:
            operation()
            print(f"  {label}: No error raised (unexpected!)")
        except ValueError as exc:
            print(f"  {label}: ValueError - {exc}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print_section("9. Summary")

    for bike in bicycles:
        print(
            f"  {bike.bicycle_id}: borrowed {bike.times_borrowed} time(s), "
            f"status = {'available' if bike.is_available else 'borrowed'}"
        )

    print_section("DEMONSTRATION COMPLETE")


if __name__ == "__main__":
    main()
