dives = []

def direction(no):
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

class dive:
    def __init__(self, num):
        self.number = num
        self.twists = 0
        self.flips = 0
        self.direction = None
        self.flying = False
        self.position = None

        
        if int(num[0]) == 5:
            self.direction = direction(num[1])
            try:
                self.twists = int(num[3]) * 0.5
            except:
                print("That is not a number")
            try:
                self.flips = int(num[2]*0.5)
            except:
                print("That is not a number")
            

        elif int(num[0]) <= 4:
            self.direction = direction(num[0])
        else:
            



def print_list():
    print("Your list is:")
    for dive in dives:
        print(dive.number+": ", dive.direction)

def main():
    print("Welcome to the Dive Number calculator")
    print("This is to help you calculate your DD list")
    no_dives = int(input("Please enter the number of dives you want to have in your list: "))
    for i in range(0,no_dives):
        new_dive = input("Please enter the dive number: ")
        correct = False
        while not(correct):
            try:
                dive(new_dive)
                dives.append(dive(new_dive))
            except:
                print("This is not a correct dive number")
    print_list()
    

if __name__ == '__main__':
    main()
