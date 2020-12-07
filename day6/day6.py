def part1():
    with open("../files/day6", "r") as f:
        groups = [group for group in f.read().split("\n\n")]
        group_totals = []
        for group in groups:
            group = group.replace("\n", "")
            yesses = set(char for char in group)
            group_totals.append(len(yesses))
        print(sum(group_totals))

def part2():
    with open("../files/day6", "r") as f:
        groups = [group for group in f.read().split("\n\n")]
        group_totals = []
        for group in groups:
            group = group.split("\n")
            group_set = set()
            for (i, person) in enumerate(group):
                if i == 0:
                    group_set = set(char for char in person)
                elif len(person) > 0:
                    group_set = group_set.intersection(set(char for char in person))
            group_totals.append(len(group_set))
        print(sum(group_totals))


part1()
part2()