import sys


def get_data(filename):
    with open(filename) as f:
        data = [line.strip().split(" | ") for line in f.readlines()]

    return data


def solve_part_1(data):
    output_values_per_line = [line[1] for line in data]
    output_values = [line.split(" ") for line in output_values_per_line]
    counter = 0
    for output_value in output_values:
        for val in output_value:
            len_val = len(val)
            if len_val in {2, 4, 3, 7}:
                counter += 1
    return counter


def solve_part_2(data):
    ...


input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = get_data(input_file)
res1 = solve_part_1(data)
print(f"Res 1: {res1}")
# res2 = solve_part_2(data)
# print(f"Res 2: {res2}")
