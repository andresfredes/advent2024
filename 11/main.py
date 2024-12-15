from math import log10


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
    return d


def part_two(data, blinks):
    results_cache = {0: 1}
    d = {int(stone): 1 for stone in data}
    for _ in range(blinks):
        d = blink_two(d, results_cache)
    sum = 0
    for value in d.values():
        sum += value
    return sum


def blink_two(data, cache):
    new_data = {}
    for stone, count in data.items():
        try:
            result = cache[stone]
        except KeyError:
            digits = int(log10(stone) + 1)
            if digits % 2 == 0:
                in_half = 10 ** (digits // 2)
                first = stone // in_half
                second = stone % in_half
                cache[stone] = first, second
                result = first, second
            else:
                result = stone * 2024
        try:
            for r in result:
                try:
                    new_data[r] += count
                except KeyError:
                    new_data[r] = count
        except TypeError:
            try:
                new_data[result] += count
            except KeyError:
                new_data[result] = count
    return new_data


if __name__ == "__main__":
    main()
