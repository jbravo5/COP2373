"""
Cinema Ticket Pre-Sale Application
- Up to 20 tickets total
- Each buyer may buy 1 to 4 tickets per purchase
- Repeats until tickets are sold out
"""

MAX_TICKETS_TOTAL = 10
MAX_TICKETS_PER_BUYER = 4


def get_ticket_request(remaining: int) -> int:
    """Prompt the user for a ticket request and return a validated integer."""
    while True:
        raw = input(f"Enter how many tickets you want to purchase? (1-{MAX_TICKETS_PER_BUYER}) "
                    f"[Remaining: {remaining}]: ").strip()

        # Basic validation: must be an integer
        try:
            requested = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Range checks
        if requested < 1:
            print("You must buy at least 1 ticket.")
            continue
        if requested > MAX_TICKETS_PER_BUYER:
            print(f"Limit is {MAX_TICKETS_PER_BUYER} tickets per buyer.")
            continue
        if requested > remaining:
            print(f"Only {remaining} ticket(s) remaining. Please enter {remaining} or less.")
            continue

        return requested


def apply_purchase(requested: int, remaining: int) -> int:
    """Apply a purchase and return updated remaining tickets."""
    remaining -= requested
    print(f"Purchase successful! Tickets remaining: {remaining}")
    return remaining


def main() -> None:
    remaining = MAX_TICKETS_TOTAL
    total_buyers = 0  # accumulator for total number of buyers (successful purchases)

    print("Welcome! Cinema ticket pre-sale is now open.")
    print(f"Total tickets available: {MAX_TICKETS_TOTAL}")
    print(f"Max per buyer: {MAX_TICKETS_PER_BUYER}\n")

    # Loop until all tickets sold
    while remaining > 0:
        requested = get_ticket_request(remaining)

        # If statement used to count buyers only when a valid purchase occurs
        if requested >= 1:
            remaining = apply_purchase(requested, remaining)
            total_buyers += 1  # accumulator update

    print("\nSOLD OUT!")
    print(f"Total number of buyers: {total_buyers}")


if __name__ == "__main__":
    main()
