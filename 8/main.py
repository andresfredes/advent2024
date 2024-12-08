from itertools import combinations
from math import ceil


def main():
    data_one = {}
    data_two = {}
    with open("8/data.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            for j, ch in enumerate(line.strip()):
                if not ch.isalnum():
                    continue
                if ch in data_one.keys():
                    data_one[ch].append([i, j])
                    data_two[ch].append([i, j])
                else:
                    data_one[ch] = [[i, j]]
                    data_two[ch] = [[i, j]]
    size = i, j
    print(f"Part One: {part_one(data_one, size)}")
    print(f"Part Two: {part_two(data_two, size)}")


def part_one(data, size):
    locations = set([])
    for ch in data.keys():
        if len(data[ch]) < 2:
            continue
        pairs = combinations(data[ch], 2)
        for pair in pairs:
            valid = get_valid_locations_one(pair, size)
            for loc in valid:
                locations.add(loc)
    return len(locations)


def get_valid_locations_one(pair, size):
    a, b = pair
    dist_vec = [b[0] - a[0], b[1] - a[1]]
    positions = [
        [a[0] - dist_vec[0], a[1] - dist_vec[1]],
        [b[0] + dist_vec[0], b[1] + dist_vec[1]],
    ]
    valid = []
    for p in positions:
        if is_valid_location(p, size):
            valid.append(f"{p[0]}-{p[1]}")
    return valid


def get_valid_locations_two(pair, size):
    a, b = pair
    valid = []
    dist_vec = [b[0] - a[0], b[1] - a[1]]
    times = size[0] if size[0] >= size[1] else size[1]
    for t in range(ceil(times)):
        dist = [dist_vec[0] * (t + 1), dist_vec[1] * (t + 1)]
        positions = [
            [a[0] - dist[0], a[1] - dist[1]],
            [a[0] + dist[0], a[1] + dist[1]],
            [b[0] + dist[0], b[1] + dist[1]],
            [b[0] - dist[0], b[1] - dist[1]],
        ]
        for p in positions:
            if is_valid_location(p, size):
                valid.append(f"{p[0]}-{p[1]}")
    return valid


def is_valid_location(pos, size):
    return pos[0] >= 0 and pos[0] <= size[0] and pos[1] >= 0 and pos[1] <= size[1]


def part_two(data, size):
    locations = set([])
    for ch in data.keys():
        if len(data[ch]) < 2:
            continue
        pairs = combinations(data[ch], 2)
        for pair in pairs:
            valid = get_valid_locations_two(pair, size)
            for loc in valid:
                locations.add(loc)
    return len(locations)


if __name__ == "__main__":
    main()
