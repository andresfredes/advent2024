import re
from functools import cmp_to_key


def part_one(rules, lines):
    middle_num_total = 0
    for line in lines:
        if is_valid_line(rules, line):
            middle_num_total += int(get_middle_num(line))
    return middle_num_total


def is_valid_line(rules, line):
    line_reversed = list(reversed(line))
    for i, num in enumerate(line_reversed):
        if num not in rules.keys():
            continue
        for num_before in line_reversed[i + 1 :]:
            if num_before in rules[num]:
                return False
    return True


def get_middle_num(line):
    return line[len(line) // 2]


def part_two(rules, lines):
    middle_num_total = 0
    for line in lines:
        if is_valid_line(rules, line):
            continue
        sorted_line = correctly_sort(line, rules)
        middle_num_total += int(get_middle_num(sorted_line))
    return middle_num_total


def correctly_sort(line, rules):
    sorted_line = line[:]
    key_func = cmp_to_key(get_cmp_func(rules))
    sorted_line.sort(key=key_func)
    return sorted_line


def get_cmp_func(rules):
    def cmp(a, b):
        if a not in rules.keys():
            return 0
        if b in rules[a]:
            return -1
        return 1

    return cmp


def is_valid_pos(num, line, rules):
    for n in line:
        if n in rules[num]:
            return False
    return True


def main():
    rules = {}
    lines = []
    with open("5/data.txt", "r") as f:
        for line in f.readlines():
            if not line[0].isdigit():
                continue
            if "|" in line:
                first, second = parse_rule(line)
                if first in rules.keys():
                    rules[first].append(second)
                else:
                    rules[first] = [second]
            if "," in line:
                lines.append(parse_line_nums(line))
    print(f"Part One: {part_one(rules, lines)}")
    print(f"Part Two: {part_two(rules, lines)}")


def strip_non_num(substring):
    return re.sub(r"[^0-9]+", "", substring)


def parse_rule(data):
    first, second = data.split("|")
    return strip_non_num(first), strip_non_num(second)


def parse_line_nums(data):
    nums = []
    for num in data.split(","):
        corrected = strip_non_num(num)
        if corrected[0].isdigit():
            nums.append(corrected)
    return nums


if __name__ == "__main__":
    main()
