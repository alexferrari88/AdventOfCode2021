from collections import defaultdict, Counter


def get_data(filename: str) -> list[int]:
    with open(filename) as f:
        raw_data = f.read()

    return [int(i) for i in raw_data.split(",")]


def solve(data, days):
    fishes_ages_counts_dict = Counter(data)

    for _ in range(days):
        copy = defaultdict(int)
        for age, count in fishes_ages_counts_dict.items():
            if age == 0:
                copy[6] += count
                copy[8] += count
            else:
                copy[age - 1] += count
        fishes_ages_counts_dict = copy

    return sum(fishes_ages_counts_dict.values())


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = solve(data, 80)
    print(f"Res 1: {res1}")
    res2 = solve(data, 256)
    print(f"Res 2: {res2}")
