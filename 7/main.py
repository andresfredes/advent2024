from itertools import product


def main():
    p1_ops = ["+", "*"]
    p2_ops = ["+", "*", "|"]
    data_one = []
    data_two = []
    with open("7/data.txt", "r") as f:
        for line in f.readlines():
            total, nums = line.split(":")
            total = int(total.strip())
            nums = nums.strip().split(" ")
            data_one.append({"total": total, "nums": [int(n) for n in nums]})
            data_two.append({"total": total, "nums": [int(n) for n in nums]})

    print(f"Part One: {part_one(data_one, p1_ops)}")
    print(f"Part Two: {part_two(data_two, p2_ops)}")


def part_one(data, operators):
    summed_totals = 0
    for line in data:
        num_operations = len(line["nums"]) - 1
        ops = product(operators, repeat=num_operations)
        for op_order in ops:
            num_a = line["nums"][0]
            for j, op in enumerate(op_order):
                num_b = line["nums"][j + 1]
                num_a = do_op(num_a, num_b, op)
                if num_a > line["total"]:
                    break
            else:
                if num_a == line["total"]:
                    summed_totals += num_a
                    break
    return summed_totals


def do_op(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "*":
            return a * b
        case "|":
            return int(str(a) + str(b))
        case _:
            print("Oh oh")
            return a + b


def part_two(data, operators):
    return part_one(data, operators)


if __name__ == "__main__":
    main()
