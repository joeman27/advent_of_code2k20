from operator import methodcaller

class Plane():
    def __init__(self):
        

class Seat():
    def __init__(self, code):
        self.code = code
        self.seat = self.getSeat()
        self.ID = self.getID()

    def getSeat(self):
        upper = 127
        lower = 0
        for char in self.code[:7]:
            if char == "F":
                upper = (upper + lower) // 2
            else:
                lower = (upper + lower) // 2 + 1
        row = lower

        upper = 7
        lower = 0
        for char in self.code[7:]:
            if char == "L":
                upper = (upper + lower) // 2
            else:
                lower = (upper + lower) // 2 + 1
        
        self.seat = (row, lower)

    def getID(self):
        (row, col) = self.seat
        return row*8 + col

    def __repr__(self):
        return f"Code: {self.code}\nSeat: {self.seat}\nID: {self.ID}\n\n"

def part1():
    with open("../files/day5", "r") as f:
        seats = [Seat(line.strip()) for line in f.readlines()]
        seats = sorted(seats, key=methodcaller("getID"))
        print(seats)


part1()