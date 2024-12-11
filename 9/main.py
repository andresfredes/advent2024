def main():
    data = ""
    with open("9/test.txt", "r") as f:
        for line in f.readlines():
            data += line

    processed_data = parse(data)
    print(f"Part One: {part_one(processed_data)}")
    print(f"Part Two: {part_two(processed_data)}")


def parse(data):
    ret = []
    current_id = 0
    for i, num in enumerate(data):
        for _ in range(int(num)):
            if i % 2 == 0:
                ret.append(current_id)
            else:
                ret.append(None)
        if i % 2 == 0:
            current_id += 1
    return ret


def part_one(data):
    d = data[:].reversed()
    running = True
    while running:
        item = d.pop()
        if item is None:
            continue

        # pop None from end
        # get last num
        # find early None pos
        # swap indexes


def part_two(data):
    pass


if __name__ == "__main__":
    main()
