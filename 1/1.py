def get_data(file: str) -> list[int]:
    with open(file) as file:
        data = [int(i) for i in file.readlines()]

    return data


def count_increases(data: list[int], windowSize: int = 1) -> int:
    count = 0
    prev_sum = sum(data[:windowSize])

    for i in range(len(data) - windowSize):
        curr_sum = prev_sum - data[i] + data[i + windowSize]
        if curr_sum > prev_sum:
            count += 1
        prev_sum = curr_sum

    return count


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = count_increases(data)
    res2 = count_increases(data, 3)

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
