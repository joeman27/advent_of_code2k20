def part1():
    with open("/home/chief/Programs/Practice/advent_of_code2k20/files/day2", "r") as f:
        valid = []
        for line in f.readlines():
            (policy, password) = line.split(": ")
            (freq, char) = policy.split()
            (low, high) = freq.split("-")
            if int(low) <= password.count(char) <= int(high):
                valid.append(password)
        print(len(valid))


def part2():
    with open("/home/chief/Programs/Practice/advent_of_code2k20/files/day2", "r") as f:
        valid = []
        for line in f.readlines():
            (policy, password) = line.split(": ")
            (pos, char) = policy.split()
            (first, second) = [int(x) for x in pos.split("-")]
            if (password[first-1] == char) != (password[second-1] == char):
                valid.append(password)

        print(len(valid))

part1()
part2()