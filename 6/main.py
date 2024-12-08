class LoopException(BaseException):
    pass


def part_one(data):
    result_data = [line[:] for line in data]
    x, y, ch = get_start_pos(result_data)
    running = True
    path = []
    while running:
        prev_ch = ch
        running, x, y, ch = move_guard(x, y, ch, result_data)
        if prev_ch == ch:
            pos = f"{x}-{y}"
            if pos in path:
                count = 0
                for p in path:
                    if p == pos:
                        count += 1
                if count > 4:
                    raise LoopException
            path.append(pos)
    return nested_count("X", result_data)


def part_two(data):
    base_data = [line[:] for line in data]
    start_x, start_y, start_ch = get_start_pos(base_data)
    loop_count = 0
    for i, line in enumerate(data):
        for j, ch in enumerate(line):
            if ch not in ["X", ".", "^", ">", "<", "v"]:
                continue
            base_data[i][j] = "O"
            if has_loop(start_x, start_y, start_ch, base_data):
                loop_count += 1
            base_data[i][j] = "."
    return loop_count


def has_loop(x, y, ch, original_data):
    data = [line[:] for line in original_data]
    running = True
    path = {}
    run_x = x
    run_y = y
    run_ch = ch
    while running:
        new_x, new_y = get_next_position(run_x, run_y, run_ch)
        if not is_within_bounds(new_x, new_y, data):
            return False
        char_in_pos = data[new_y][new_x]
        if char_in_pos == ".":
            data[run_y][run_x] = "."
            data[new_y][new_x] = run_ch
            pos = f"{run_x}-{run_y}"
            run_x = new_x
            run_y = new_y
            if pos in path.keys():
                path[pos] += 1
                if path[pos] > 4:
                    return True
            else:
                path[pos] = 1
        else:
            run_ch = get_next_char(run_ch)
            data[run_y][run_x] = "."


def get_start_pos(data: list[list[str]]):
    guard = ["^", "<", ">", "v"]
    for i, line in enumerate(data):
        for ch in guard:
            if ch in line:
                return line.index(ch), i, ch


def move_guard(x, y, ch, data):
    running = True
    new_ch = ch
    new_x, new_y = get_next_position(x, y, new_ch)
    if not is_within_bounds(new_x, new_y, data):
        data[y][x] = "X"
        running = False
    else:
        char_in_pos = data[new_y][new_x]
        if char_in_pos in ["X", "."]:
            data[y][x] = "X"
            data[new_y][new_x] = new_ch
        else:
            new_ch = get_next_char(ch)
            new_x = x
            new_y = y
    return running, new_x, new_y, new_ch


def is_within_bounds(x, y, data):
    width = len(data[0])
    height = len(data)
    within_bounds = x >= 0 and y >= 0 and x < width and y < height
    return within_bounds


def get_next_char(ch):
    match ch:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"
        case _:
            print("something went wrong with guard turning")
            return "^"


def get_next_position(x, y, ch):
    match ch:
        case "^":
            return x, y - 1
        case "<":
            return x - 1, y
        case ">":
            return x + 1, y
        case "v":
            return x, y + 1
        case _:
            print("Something went wrong with char handling")
            return x, y


def nested_count(ch, data):
    count = 0
    for line in data:
        for char in line:
            if char == ch:
                count += 1
    return count


def main():
    data = []
    with open("6/data.txt", "r") as f:
        for line in f.readlines():
            split_line = []
            for ch in line.strip():
                split_line.append(ch)
            data.append(split_line)
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
