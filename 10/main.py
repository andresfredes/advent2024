def main():
    data = []
    trailheads = []
    with open("10/data.txt", "r") as f:
        for y, line in enumerate(f.readlines()):
            temp = []
            for x, ch in enumerate(line.strip()):
                if ch == "0":
                    trailheads.append([x, y])
                try:
                    temp.append(int(ch))
                except ValueError:
                    temp.append(ch)
            data.append(temp)
    print(f"Part One: {part_one(data, trailheads)}")
    print(f"Part Two: {part_two(data, trailheads)}")


def part_one(data, trailheads):
    sum = 0
    for t in trailheads:
        node = Node(x=t[0], y=t[1], value=data[t[1]][t[0]])
        node.walk_trail(data)
        locs = node.get_distinct_high_locations()
        if locs is not None:
            sum += len(locs)
    return sum


def part_two(data, trailheads):
    sum = 0
    for t in trailheads:
        node = Node(x=t[0], y=t[1], value=data[t[1]][t[0]])
        node.walk_trail(data)
        locs = node.get_num_paths()
        sum += locs
    return sum


class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.children: list[Node] = []

    def walk_trail(self, data):
        if self.value == 9:
            return
        for n in check_adj_neighbours(data, (self.x, self.y)):
            child = Node(x=n[0], y=n[1], value=data[n[1]][n[0]])
            self.children.append(child)
        for c in self.children:
            c.walk_trail(data)

    def get_distinct_high_locations(self):
        if self.value == 9:
            return [str(self)]
        if len(self.children) == 0:
            return None
        end_locations = set([])
        for c in self.children:
            end_loc_iter = c.get_distinct_high_locations()
            if end_loc_iter is None:
                continue
            for item in end_loc_iter:
                if item is not None:
                    end_locations.add(item)
        if len(end_locations) > 0:
            return end_locations
        return None

    def get_num_paths(self):
        if self.value == 9:
            return 1
        if len(self.children) == 0:
            return 0
        complete_paths = 0
        for c in self.children:
            complete_paths += c.get_num_paths()
        return complete_paths

    def __str__(self):
        return f"{self.x}-{self.y}"


def check_adj_neighbours(data, loc):
    target_value = data[loc[1]][loc[0]] + 1
    next_steps = []
    locs = [
        [loc[0] - 1, loc[1]],
        [loc[0] + 1, loc[1]],
        [loc[0], loc[1] - 1],
        [loc[0], loc[1] + 1],
    ]
    for x, y in locs:
        if not is_valid_location(data, x, y):
            continue
        if data[y][x] == target_value:
            next_steps.append([x, y])
    return next_steps


def check_all_neighbours(data, loc):
    target_value = data[loc[1]][loc[0]] + 1
    next_steps = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            x = loc[0] + i
            y = loc[1] + j
            if not is_valid_location(data, x, y):
                continue
            if data[y][x] == target_value:
                next_steps.append([x, y])
    return next_steps


def is_valid_location(data, x, y):
    if y >= len(data) or y < 0 or x >= len(data[0]) or x < 0:
        return False
    if data[y][x] == ".":
        return False
    return True


if __name__ == "__main__":
    main()
