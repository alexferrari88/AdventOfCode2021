import pandas as pd


def get_data(file: str) -> list[list[int]]:
    with open(file) as file:
        data = []
        raw_data = [list(line.strip()) for line in file.readlines()]
        for line in raw_data:
            line_list = []
            for i in line:
                line_list.append(int(i))
            data.append(line_list)

    return data


def most_common(df, tie_val=None, index=0):
    n_columns = df.shape[1]
    if tie_val is None:
        return [int(df[i].mode()) for i in range(n_columns)]

    n_0 = int(df.loc[df[index] == 0, [index]].value_counts())
    n_1 = int(df.loc[df[index] == 1, [index]].value_counts())
    if n_1 == n_0:
        return tie_val

    return 0 if n_0 > n_1 else 1


def least_common(df, tie_val=None, index=0):
    n_columns = df.shape[1]
    if tie_val is None:
        return [int(df[i].value_counts().idxmin()) for i in range(n_columns)]

    n_0 = int(df.loc[df[index] == 0, [index]].value_counts())
    n_1 = int(df.loc[df[index] == 1, [index]].value_counts())
    if n_1 == n_0:
        return tie_val

    return 0 if n_0 < n_1 else 1


def calculate_int_from_list_bin(binary_n_list: list[int]) -> int:
    return int("".join(str(i) for i in binary_n_list), 2)


def solve_part_1(data):
    df = pd.DataFrame(data)
    gamma = most_common(df)
    epsilon = least_common(df)
    gamma = calculate_int_from_list_bin(gamma)
    epsilon = calculate_int_from_list_bin(epsilon)

    return gamma * epsilon


def solve_part_2(data):
    df = pd.DataFrame(data)
    o2_df = df.copy()
    co2_df = df.copy()
    n_columns = df.shape[1]

    for i in range(n_columns):
        most_common_in_df = most_common(df=o2_df, tie_val=1, index=i)
        o2_df = o2_df[o2_df[i] == most_common_in_df]
        if len(o2_df) == 1:
            break

    for i in range(n_columns):
        least_common_in_df = least_common(df=co2_df, tie_val=0, index=i)
        co2_df = co2_df[co2_df[i] == least_common_in_df]
        if len(co2_df) == 1:
            break

    o2_int = calculate_int_from_list_bin(o2_df.values[0].tolist())
    co2_int = calculate_int_from_list_bin(co2_df.values[0].tolist())

    return o2_int * co2_int


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = solve_part_1(data)
    res2 = solve_part_2(data)
    print(f"Res 1: {res1}")
    print(f"Res 2: {res2}")
