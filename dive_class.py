from helper import direction, position

class dive:
    def __init__(self, num):
        self.number = num
        self.twists = 0
        self.flips = 0
        self.direction = None
        self.flying = False
        self.position = None
        self.bad = False


    def set(self):
        self.bad = False
        if int(self.number[0]) == 5: #Twisters
            self.direction = direction(self.number[1])
            try:
                self.twists = float(int(self.number[3]) * 0.5)
            except:
                print("That is not a number")
            try:
                self.flips = float(int(self.number[2])*0.5)
            except:
                print("That is not a number")
            self.position = position(self.number[4])
        elif int(self.number[0]) <= 4:
            self.direction = direction(self.number[0])
            try:
                self.flips = float(int(self.number[2])*0.5)
            except:
                print("Flips: That is not a number")
            self.position = position(self.number[3])
            if self.number[1] == '1':
                self.flying = True
        else:
            print("This is not a valid dive number.")
            self.number = input("Please enter a new number in the correct dive format: ")
            self.bad = True