def part1():
    with open("/home/chief/Programs/Practice/advent_of_code2k20/files/day1", "r") as f:
        lines = [int(x) for x in f.readlines()]
        for num in lines:
            if 2020 - num in lines:
                print(num * (2020-num))

def part2():
    with open("/home/chief/Programs/Practice/advent_of_code2k20/files/day1", "r") as f:
        lines = [int(x) for x in f.readlines()]
        for num in lines:
            for num2 in lines:
                for num3 in lines:
                    if num + num2 + num3 == 2020:
                        print(num * num2 * num3)

part1()
part2()