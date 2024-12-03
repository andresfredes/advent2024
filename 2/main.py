def part_one(reports):
    safe_reports = 0
    for report in reports:
        safe = is_safe_one(report)
        if safe:
            safe_reports += 1
    return safe_reports


def is_safe_one(report):
    first = None
    is_ascending = None
    for level in report:
        second = level
        if first is None:
            first = level
            continue
        diff = second - first
        first = level
        if diff == 0:
            return False
        if diff < 0:
            if diff < -3:
                return False
            if is_ascending is None:
                is_ascending = False
            if is_ascending:
                return False
            continue
        if diff > 3:
            return False
        if is_ascending is None:
            is_ascending = True
            continue
        if not is_ascending:
            return False
    return True


def part_two(reports):
    safe_reports = 0
    for report in reports:
        safe = is_safe_two(report)
        if safe:
            safe_reports += 1
    return safe_reports


def is_safe_two(report):
    if test_report(report):
        return True
    print(f"False with dampener for {report}")
    for i, _ in enumerate(report):
        temp_report = [x for idx, x in enumerate(report) if idx != i]
        if test_report(temp_report):
            return True
    print("False")
    return False


def test_report(report):
    first = None
    is_ascending = None
    for level in report:
        second = level
        if first is not None:
            result = test_difference(first, second, is_ascending)
            is_ascending = result["is_ascending"]
            if not result["is_safe"]:
                return False
        first = level
    return True


def test_difference(first, second, is_ascending):
    ret_value = {"is_ascending": is_ascending, "is_safe": False}
    diff = second - first
    if diff == 0:
        return ret_value

    if diff < 0:
        if diff < -3:
            return ret_value
        if is_ascending is None:
            ret_value["is_ascending"] = False
        if not ret_value["is_ascending"]:
            ret_value["is_safe"] = True
        return ret_value

    if diff > 3:
        return ret_value
    if is_ascending is None:
        ret_value["is_ascending"] = True
    if ret_value["is_ascending"]:
        ret_value["is_safe"] = True
    return ret_value


def main():
    reports = []
    with open("2/data.txt", "r") as f:
        for line in f.readlines():
            reports.append([int(x) for x in line.split()])
    print(f"Part One: {part_one(reports)}")
    print(f"Part Two: {part_two(reports)}")


if __name__ == "__main__":
    main()
