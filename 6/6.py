from collections import defaultdict, Counter
import time


class Fish:
    PARENT_INITIAL_TIMER = 6
    CHILD_INITIAL_TIMER = 8

    def __init__(self, timer: int = PARENT_INITIAL_TIMER, birthday: int = 0) -> None:
        self.timer = timer
        self.__birthday = birthday

    @classmethod
    def spawn(cls, birthday: int):
        return Fish(cls.CHILD_INITIAL_TIMER, birthday)

    def age(self, n_days: int = 1):
        if self.timer == 0:
            self.timer = self.PARENT_INITIAL_TIMER
            return
        self.timer -= n_days
        return

    @property
    def birthday(self) -> int:
        return self.__birthday

    def __str__(self) -> str:
        return str(self.timer)


def get_data(filename: str) -> list[int]:
    with open(filename) as f:
        raw_data = f.read()

    return [int(i) for i in raw_data.split(",")]


def solve_part_1(data, days):
    start = time.time()
    fishes: list[Fish] = [Fish(i) for i in data]

    for day in range(days):
        for fish in fishes:
            if fish.birthday == day and fish.timer == Fish.CHILD_INITIAL_TIMER:
                continue
            if fish.timer == 0:
                fishes.append(fish.spawn(day))
            fish.age()
    end = time.time()
    print(f"1: {(end-start)}")
    return len(fishes)


def solve_part_2(data, days):
    start = time.time()
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

    end = time.time()
    print(f"1: {(end-start)}")
    return sum(fishes_ages_counts_dict.values())


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = solve_part_1(data, 80)
    print(f"Res 1: {res1}")
    res2 = solve_part_2(data, 256)
    print(f"Res 2: {res2}")
