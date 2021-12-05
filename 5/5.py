﻿import numpy as np
import pandas as pd


def get_data(filename):
    with open(filename) as f:
        raw_data = [line.strip().split(" -> ") for line in f.readlines()]

    start_xy = []
    end_xy = []
    for row in raw_data:
        start_xy.append([int(i) for i in row[0].split(",")])
        end_xy.append([int(i) for i in row[1].split(",")])

    return (start_xy, end_xy)


def solve_part_1(start_xy, end_xy):
    if len(start_xy) != len(end_xy):
        raise ValueError
    n = len(start_xy)

    start_maxtrix = np.array(start_xy, dtype=np.int32)
    end_maxtrix = np.array(end_xy, dtype=np.int32)

    max_start_x, max_start_y = start_maxtrix.max(axis=0)
    max_end_x, max_end_y = end_maxtrix.max(axis=0)
    max_x = max([max_start_x, max_end_x])
    max_y = max([max_start_y, max_end_y])

    final_matrix = np.zeros((max_y + 1, max_x + 1), dtype=np.int32)

    for i in range(n):
        start_x = start_maxtrix[i][0]
        start_y = start_maxtrix[i][1]
        end_x = end_maxtrix[i][0]
        end_y = end_maxtrix[i][1]
        if start_x == end_x:
            x = start_x
            ys = [n for n in range(min([start_y, end_y]), max([start_y, end_y]) + 1)]
            for y in ys:
                final_matrix[y, x] += 1
        elif start_y == end_y:
            y = start_y
            xs = [n for n in range(min([start_x, end_x]), max([start_x, end_x]) + 1)]
            for x in xs:
                final_matrix[y, x] += 1
        else:
            continue

    result = []
    for row in final_matrix:
        for n in row:
            if n >= 2:
                result.append(n)
    return len(result)


if __name__ == "__main__":
    start_xy, end_xy = get_data("input.txt")
    res1 = solve_part_1(start_xy, end_xy)
    print(f"Res 1: {res1}")
