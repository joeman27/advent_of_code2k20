def part1():
    trees = 0
    with open("../files/day3", "r") as f:
        col = 0
        for row_num, row in enumerate(f.readlines()):
            if row[col] == "#":
                trees += 1
            col = (col+3) % 31
    print(trees)

def part2():
    from functools import reduce
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_totals = []
    for slope in slopes:
        trees = 0
        with open("../files/day3", "r") as f:
            col = 0
            row = 0
            tree_map = f.readlines()
            while (row < len(tree_map)):
                if tree_map[row][col] == "#":
                    trees += 1
                col = (col+slope[0]) % 31
                row += slope[1]
        tree_totals.append(trees)
    print(f"{tree_totals[0]} * {tree_totals[1]} * {tree_totals[2]} * {tree_totals[3]} * {tree_totals[4]} = {reduce(lambda x, y: x * y, tree_totals)}")

# part1()
part2()