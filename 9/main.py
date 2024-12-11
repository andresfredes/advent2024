def main():
    data = ""
    with open("9/data.txt", "r") as f:
        for line in f.readlines():
            data += line

    # processed_data = parse(data)
    # print(f"Part One: {part_one(processed_data)}")
    processed_data = parse_as_files(data)
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


def parse_as_files(data):
    ret = []
    current_id = 0
    for i, num in enumerate(data):
        if i % 2 == 0:
            ret.append({"id": current_id, "size": int(num)})
            current_id += 1
        else:
            ret.append({"id": None, "size": int(num)})
    return ret


def part_one(data):
    d = data[:]
    while True:
        item = d.pop()
        if item is None:
            continue
        for i, value in enumerate(d):
            if value is None:
                d[i] = item
                break
        else:
            d.append(item)
            break
    sum = 0
    for i, num in enumerate(d):
        sum += i * num
    return sum


def part_two(data: list):
    d = data[:]
    largest_id = 0
    for item in reversed(d):
        if item["id"] is None:
            continue
        else:
            largest_id = item["id"]
            break
    while largest_id >= 0:
        i, item = index_item_from_id(largest_id, d)
        for index in range(i):
            if d[index]["id"] is not None or d[index]["size"] < item["size"]:
                continue
            if d[index]["size"] == item["size"]:
                d[index]["id"] = item["id"]
                item["id"] = None
            else:
                d[index]["size"] -= item["size"]
                copy = {"id": item["id"], "size": item["size"]}
                item["id"] = None
                d = [*d[:index], copy, *d[index:]]
            break
        largest_id -= 1
    sum = 0
    i = -1
    for item in d:
        for _ in range(item["size"]):
            i += 1
            if item["id"] is None:
                continue
            sum += i * item["id"]
    return sum


def index_item_from_id(id, data):
    for i, item in enumerate(data):
        if item["id"] == id:
            return i, item


if __name__ == "__main__":
    main()
