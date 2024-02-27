from dive_class import dive

dives = []

def print_list():
    print("Your list is:")
    for dive in dives:
        print(dive.number+": ", dive.direction, end = " ")
        if dive.flying:
            print("Flying", end = " ")
        
        if dive.flips == 0.5:
            print("Dive", end= " ")
        elif dive.flips == 1:
            print("1 Somersault", end = " ")
        else:
            print(str(dive.flips), "Somersaults", end= " ")
        
        if dive.twists > 0:
            if dive.twists == 1:
                print("1 Twist", end=" ")
            else:
                print(dive.twists, "Twists", end= " ")
        print(dive.position)
        

def main():
    print("Welcome to the Dive Number calculator")
    print("This is to help you calculate your DD list")
    no_dives = int(input("Please enter the number of dives you want to have in your list: "))
    for i in range(0,no_dives):
        new_dive = input("Please enter the dive number: ")
        correct = False
        while not(correct):
            try:
                new_dive_no = dive(new_dive)
                dives.append(new_dive_no)
                new_dive_no.set()
                correct = True
            except:
                print("This is not a correct dive number")
                print()
        
    print_list()
    

if __name__ == '__main__':
    main()
