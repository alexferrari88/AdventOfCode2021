def get_data(filename):
    with open(filename) as f:
        data = [int(i) for i in f.read().strip().split(",")]

    return data


def solve_part_1(data):
    ...


def solve_part_2(data):
    ...


data = get_data("input.txt")
res1 = solve_part_1(data)
print(f"Res 1: {res1}")
res2 = solve_part_2(data)
print(f"Res 2: {res2}")
