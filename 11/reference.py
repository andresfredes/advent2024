"""
Earlier attempts, retained for comparison and reflection
Note: bad naming patterns due to duplication of functions
"""

from functools import cache
from math import log10


def attempt_one(data, blinks):
    d = data[:]
    for _ in range(blinks):
        d = blink_two(d)
    return len(d)


def blink_two(data):
    d = []
    for stone in data:
        for i in apply_rules(stone):
            d.append(i)
    return d


@cache
def apply_rules(data):
    if int(data) == 0:
        return ["1"]
    if len(data) % 2 == 0:
        half = len(data) // 2
        return [str(int(data[:half])), str(int(data[half:]))]
    return [str(int(data) * 2024)]


def attempt_two(data, blinks):
    d = [{"value": int(s), "count": blinks} for s in reversed(data)]
    result = []
    stone = d.pop()
    while stone is not None:
        if stone["count"] == 0:
            result.append(stone)
        else:
            for item in apply_rules_two(stone):
                d.append(item)
        try:
            stone = d.pop()
        except IndexError:
            stone = None
    return len(result)


def apply_rules_two(data):
    count = data["count"] - 1
    if data["value"] == 0:
        return [{"value": 1, "count": count}]
    digits = int(log10(data["value"]) + 1)
    if digits % 2 == 0:
        in_half = 10 ** (digits // 2)
        return [
            {"value": data["value"] % in_half, "count": count},
            {"value": data["value"] // in_half, "count": count},
        ]
    return [{"value": data["value"] * 2024, "count": count}]


def attempt_three(data, blinks):
    my_cache = {0: 1}
    d = [{"value": int(s), "count": blinks} for s in reversed(data)]
    result = 0
    stone = d.pop()
    while stone is not None:
        if stone["count"] == 0:
            result += 1
            try:
                stone = d.pop()
            except IndexError:
                stone = None
            continue
        stone["count"] -= 1
        try:
            value = my_cache[stone["value"]]
        except KeyError:
            digits = int(log10(stone["value"]) + 1)
            if digits % 2 == 0:
                in_half = 10 ** (digits // 2)
                first = stone["value"] // in_half
                second = stone["value"] % in_half
                my_cache[stone["value"]] = first, second
                value = first, second
            else:
                value = stone["value"] * 2024
        try:
            stone["value"] = value[0]
            d.append({"value": value[1], "count": stone["count"]})
        except TypeError:
            stone["value"] = value
    return result
