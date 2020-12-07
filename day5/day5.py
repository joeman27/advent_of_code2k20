def get_pos(code):
    upper = 127
    lower = 0
    for char in code[:7]:
        if char == "F":
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
    row = lower

    upper = 7
    lower = 0
    for char in code[7:]:
        if char == "L":
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
    col = lower

    return (row, col)

def get_ID(code):
    (row, col) = get_pos(code)
    return row*8 + col

def get_empties(codes):
    seats = {(i, j): False for j in range(8) for i in range(128)}
    for code in codes:
        pos = get_pos(code)
        seats[pos] = code
    return seats


def part1():
    with open("../files/day5", "r") as f:
        print(f"Max: {max([get_ID(code.strip()) for code in f.readlines()])}")

def part2():
    with open("../files/day5", "r") as f:
        with open("day_5_output", "w") as w:
            seats = get_empties([code.strip() for code in f.readlines()])
            print(seats)

part1()
part2()