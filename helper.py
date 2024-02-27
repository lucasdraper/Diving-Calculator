def direction(no):
    no = int(no)
    if no == 1:
        return "Forward"
    elif no == 2:
        return "Back"
    elif no == 3:
        return "Reverse"
    elif no == 4:
        return "Inward"
    else:
        return None

def position(let):
    if let == 'A' or let == 'a':
        return "Straight"
    elif let == 'B' or let == 'b':
        return "Pike"
    elif let == 'C' or let == 'c':
        return "Tuck"
    elif let == 'D' or let == 'd':
        return "Free"
    else:
        return None
