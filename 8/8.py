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
    for i, digit_pattern in enumerate(digits_patterns):
        if len(digit_pattern) == 2:
            one = set(digit_pattern)
            to_return[1] = one
        elif len(digit_pattern) == 4:
            four = set(digit_pattern)
            to_return[4] = four
        elif len(digit_pattern) == 3:
            seven = set(digit_pattern)
            to_return[7] = seven
        elif len(digit_pattern) == 7:
            eight = set(digit_pattern)
            to_return[8] = eight

    zero_or_six_or_nine = [set(v) for v in digits_patterns if len(v) == 6]
    two_or_three_or_five = [set(v) for v in digits_patterns if len(v) == 5]
    four_union_seven = four.union(seven)
    for i, val in enumerate(zero_or_six_or_nine):
        if len(val.difference(four_union_seven)) == 1:
            nine = zero_or_six_or_nine.pop(i)
            to_return[9] = nine
            break
    zero_or_six = zero_or_six_or_nine.copy()
    for i, val in enumerate(zero_or_six):
        if len(val.difference(one)) == 4:
            zero = zero_or_six.pop(i)
            to_return[0] = zero
            break
    six = zero_or_six[0]
    to_return[6] = six
    for i, val in enumerate(two_or_three_or_five):
        if len(val.difference(one)) == 3:
            three = two_or_three_or_five.pop(i)
            to_return[3] = three
            break
    two_or_five = two_or_three_or_five.copy()
    for i, val in enumerate(two_or_five):
        if four.union(val) == nine:
            five = two_or_five.pop(i)
            to_return[5] = five
    two = two_or_five[0]
    to_return[2] = two

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
