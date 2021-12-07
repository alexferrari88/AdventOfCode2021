import math
from statistics import mean, median


def get_data(filename):
    with open(filename) as f:
        data = [int(i) for i in f.read().strip().split(",")]

    return data


def solve_part_1(data):
    num_at_center = int(median(sorted(data)))
    return sum(abs(i - num_at_center) for i in data)


def solve_part_2(data):
    most_common = math.floor(mean(data))
    print(most_common)
    return sum(abs(p - most_common) + sum(range(abs(p - most_common))) for p in data)


data = get_data("input.txt")
res1 = solve_part_1(data)
print(f"Res 1: {res1}")
res2 = solve_part_2(data)
print(f"Res 2: {res2}")
