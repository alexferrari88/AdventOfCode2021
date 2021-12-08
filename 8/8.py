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


def decode_signal_pattern(digits_patterns):
    to_return = [None] * len(digits_patterns)
    for digit_pattern in digits_patterns:
        set_digits = set(digit_pattern)
        if len(digit_pattern) == 2:
            to_return[1] = set_digits
        elif len(digit_pattern) == 4:
            to_return[4] = set_digits
        elif len(digit_pattern) == 3:
            to_return[7] = set_digits
        elif len(digit_pattern) == 7:
            to_return[8] = set_digits

    for digit_pattern in digits_patterns:
        set_digits = set(digit_pattern)

        if len(digit_pattern) in {2, 4, 3, 7}:
            continue

        # the number can be either 0 or 6 or 9
        if len(digit_pattern) == 6:

            # the shape of 4 and 7 combined give lack 1 piece, compared to the shape of 9
            if len(set_digits.difference(to_return[4].union(to_return[7]))) == 1:
                to_return[9] = set_digits

            # the shape of 1 lacks 4 pieces, compared to the shape of 0
            elif len(set_digits.difference(to_return[1])) == 4:
                to_return[0] = set_digits
            else:
                to_return[6] = set_digits

        # the number can be either 2 or 3 or 5
        elif len(digit_pattern) == 5:

            # the shape of  1 lacks 3 pieces, when compared with the shape of 3
            if len(set_digits.difference(to_return[1])) == 3:
                to_return[3] = set_digits

            # the shapes of 4 and 5 have 3 pieces in common
            elif len(set_digits.intersection(to_return[4])) == 3:
                to_return[5] = set_digits
            else:
                to_return[2] = set_digits

    return to_return


def solve_part_2(data):
    signal_patterns_list = [v[0].split(" ") for v in data]
    output_values_list = [v[1].split(" ") for v in data]
    counter = 0
    for row_num, signal_pattern in enumerate(signal_patterns_list):
        signal = decode_signal_pattern(signal_pattern)
        num_string = ""
        for val in output_values_list[row_num]:
            num_string += str(signal.index(set(val)))
        counter += int(num_string)

    return counter


input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = get_data(input_file)
res1 = solve_part_1(data)
print(f"Res 1: {res1}")
res2 = solve_part_2(data)
print(f"Res 2: {res2}")
