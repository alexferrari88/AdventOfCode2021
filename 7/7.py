from statistics import median


def get_data(filename):
    with open(filename) as f:
        data = [int(i) for i in f.read().strip().split(",")]

    return data


def solve_part_1(data):
    num_at_center = int(median(sorted(data)))
    print(num_at_center)
    return sum(abs(i - num_at_center) for i in data)


data = get_data("input.txt")
res1 = solve_part_1(data)
print(f"Res 1: {res1}")
