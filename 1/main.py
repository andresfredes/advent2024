def part_one(first, second):
    cumul_distance = 0
    for a, b in zip(sorted(first), sorted(second)):
        distance = abs(int(a) - int(b))
        cumul_distance += distance
    return cumul_distance


def part_two(first, second):
    second_lookup = {}
    for num in second:
        try:
            second_lookup[num] += 1
        except KeyError:
            second_lookup[num] = 1
    cumul_distance = 0
    for num in first:
        try:
            distance = second_lookup[num] * int(num)
        except KeyError:
            distance = 0
        cumul_distance += distance
    return cumul_distance


def main():
    first = []
    second = []
    with open("1/data.txt", "r") as f:
        for line in f.readlines():
            a, b = line.split()
            first.append(a)
            second.append(b)
    print(f"Part One: {part_one(first, second)}")
    print(f"Part Two: {part_two(first, second)}")


if __name__ == "__main__":
    main()
