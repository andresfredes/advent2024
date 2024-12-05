import re


def part_one(data):
    columns = get_columns(data)
    forward_diag = get_forward_diag(data)
    backward_diag = get_backward_diag(data)
    count = 0
    for substr in [*data, *columns, *forward_diag, *backward_diag]:
        count += count_pattern(substr, ["XMAS", "SAMX"])
    return count


def get_columns(data):
    cols = []
    for i, _ in enumerate(data[0]):
        col = ""
        for line in data:
            if i >= len(line):
                continue
            col += line[i]
        cols.append(col)
    return cols


def get_forward_diag(data):
    diags = []
    max_iter_length = len(data) + len(data[0])
    for i in range(max_iter_length):
        diag = ""
        for j, line in enumerate(data):
            x_pos = i - j
            if x_pos < 0 or x_pos >= len(data):
                continue
            diag += line[x_pos]
        diags.append(diag)
    return diags


def get_backward_diag(data):
    return get_forward_diag(list(reversed(data)))


def count_pattern(line, patterns):
    count = 0
    for pattern in patterns:
        regex = re.compile(pattern)
        count += len(regex.findall(line))
    return count


def part_two(data):
    count = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != "A":
                continue
            if check_diags(data, i, j):
                count += 1
    return count


def check_diags(data, i, j):
    if i + 1 >= len(data) or i - 1 < 0 or j + 1 >= len(data[i]) or j - 1 < 0:
        return False
    valid = ["M", "S"]
    nw = data[i - 1][j - 1]
    ne = data[i - 1][j + 1]
    sw = data[i + 1][j - 1]
    se = data[i + 1][j + 1]
    for char in [nw, se, ne, sw]:
        if char not in valid:
            return False
    if nw == se or ne == sw:
        return False
    return True


def main():
    data = []
    with open("4/data.txt", "r") as f:
        for line in f.readlines():
            data.append(line)

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
