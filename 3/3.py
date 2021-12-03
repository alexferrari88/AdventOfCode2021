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


def solve_part_1(data):
    df = pd.DataFrame(data)
    gamma = []
    epsilon = []
    n_columns = df.shape[1]
    for i in range(n_columns):
        gamma.append(int(df[i].mode()))
    for i in range(n_columns):
        epsilon.append(int(df[i].value_counts().idxmin()))

    gamma = int("".join(str(i) for i in gamma), 2)
    epsilon = int("".join(str(i) for i in epsilon), 2)

    return gamma * epsilon


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = solve_part_1(data)
    print(f"Res 1: {res1}")
