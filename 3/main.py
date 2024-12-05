import re


def part_one(data):
    num_pairs = []
    for line in data:
        matches = get_multiple_groups(line)
        if matches is None:
            continue
        for match in matches:
            if match is None:
                continue
            nums = extract_nums(match)
            num_pairs.append(nums)
    return add_multiples(num_pairs)


def part_two(data):
    num_pairs = []
    currently_enabled = True
    for line in data:
        # print(f"Before: {line}")
        print(f"Len before: {len(line)}")
        currently_enabled, updated_line = remove_disabled(line, currently_enabled)
        # print(f"After: {updated_line}")
        print(f"Len after: {len(updated_line)}")
        matches = get_multiple_groups(updated_line)
        if matches is None:
            continue
        for match in matches:
            if match is None:
                continue
            nums = extract_nums(match)
            num_pairs.append(nums)
    return add_multiples(num_pairs)


def remove_disabled(data, currently_enabled):
    p_dont = r"don't()"
    dont_re = re.compile(p_dont)
    dont_iter = dont_re.finditer(data)
    dont_starts = []
    for match in dont_iter:
        _, start = match.span()
        dont_starts.append(start)
    print(f"Donts: {dont_starts}")
    p_do = r"do()"
    do_re = re.compile(p_do)
    do_iter = do_re.finditer(data)
    do_starts = []
    for match in do_iter:
        _, start = match.span()
        do_starts.append(start)
    print(f"Dos:  {do_starts}")
    all_starts = sorted([*do_starts, *dont_starts])
    enabled = currently_enabled
    important_pos = []
    for pos in all_starts:
        if pos in do_starts and enabled:
            continue
        if pos in dont_starts and not enabled:
            continue
        important_pos.append(pos)
        enabled = not enabled
    important_pos = [0, *important_pos]
    is_odd = len(important_pos) % 2
    if is_odd:
        important_pos.append(len(data) - 1)
    print(f"Important: {important_pos}")
    it = iter(important_pos)
    result_data = ""
    for start, stop in zip(it, it):
        result_data += data[start:stop]
    return enabled, result_data


def get_multiple_groups(data):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    regex = re.compile(pattern)
    return regex.findall(data)


def extract_nums(data):
    pattern = r"\d{1,3}"
    regex = re.compile(pattern)
    return regex.findall(data)


def add_multiples(num_pairs):
    sum = 0
    for a, b in num_pairs:
        sum += int(a) * int(b)
    return sum


def main():
    data = []
    with open("3/data.txt", "r") as f:
        data.append(f.read())
        # for line in f.read():
        #     data.append(line)

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
