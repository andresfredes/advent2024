from functools import cache


def main():
    data = []
    with open("11/data.txt", "r") as f:
        for line in f.readlines():
            for stone in line.strip().split(" "):
                data.append(stone)
    blinks = 25
    print(f"Part One: {part_one(data, blinks)}")
    blinks = 75
    print(f"Part Two: {part_two(data, blinks)}")


def part_one(data, blinks):
    d = data[:]
    for _ in range(blinks):
        d = blink(d)
    return len(d)


def blink(data):
    d = []
    for stone in data:
        if int(stone) == 0:
            d.append("1")
            continue
        if len(stone) % 2 == 0:
            d.append(str(int(stone[: len(stone) // 2])))
            d.append(str(int(stone[len(stone) // 2 :])))
            continue
        d.append(str(int(stone) * 2024))
    # print(" ".join(d))
    return d


def part_two(data, blinks):
    d = data[:]
    for _ in range(blinks):
        d = blink_two(d)
    return len(d)


def blink_two(data):
    d = []
    for stone in data:
        for i in apply_rules(stone):
            d.append(i)
    return d


@cache
def apply_rules(data):
    if int(data) == 0:
        return ["1"]
    if len(data) % 2 == 0:
        half = len(data) // 2
        return [str(int(data[:half])), str(int(data[half:]))]
    return [str(int(data) * 2024)]


if __name__ == "__main__":
    main()
