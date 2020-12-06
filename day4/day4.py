def part1():
    import re

    reqs = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    
    with open("../files/day4", "r") as f:
        entries = f.read().split("\n\n")
        valid = 0
        for entry in entries:
            fields = re.split("\n|\s", entry)
            valid += 1 if all([any(req in field for field in fields) for req in reqs]) else 0
    print(valid)
    
def part2():
    import re

    # Required fields
    reqs = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    # Validation criteria for fields
    # validations.items() return True if validation successful, False otherwise
    validations = { "byr": lambda x: re.match(r"\d{4}\b", x) != None and 1920 <= int(x) <= 2002,
                    "iyr": lambda x: re.match(r"\d{4}\b", x) != None and 2010 <= int(x) <= 2020,
                    "eyr": lambda x: re.match(r"\d{4}\b", x) != None and 2020 <= int(x) <= 2030,
                    "hgt": lambda x: re.match(r"\d+(cm|in)\b", x) != None and 
                        (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
                        (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
                    "hcl": lambda x: re.match(r"#(\d|[a-f]){6}\b", x) != None,
                    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
                    "pid": lambda x: re.match(r"\d{9}\b", x) != None,
                    "cid": lambda x: True
    }
    
    with open("../files/day4", "r") as f:
        entries = f.read().split("\n\n")
        valid_entries = 0

        for entry in entries:
            # byr:1995 hcl:#1a2b3c -> {byr: 1995, hcl: #1a2b3c}
            fields = {field[:3]: field[4:] for field in re.split("\n|\s", entry.strip())}
            # Check all required fields are contained in each list of fields
            present = all([any(req in field for field in fields.keys()) for req in reqs])
            if present:
                valid_flag = True
                for (key, field) in fields.items():
                    valid_flag *= bool(validations[key](field))
                valid_entries += int(valid_flag)

    print(valid_entries)

part1()
part2()