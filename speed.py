def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    if is_birthday:
        if speed <= 65:
            return "No Ticket"
        elif speed >= 86:
            return "Big Ticket"
        else:
            return "Small Ticket"
    else:
        if speed <= 60:
            return "No Ticket"
        elif speed >= 81:
            return "Big Ticket"
        else:
            return "Small Ticket"



# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"