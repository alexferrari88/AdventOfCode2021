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
    def birthday(self):
        return self.__birthday

    def __str__(self) -> str:
        return str(self.timer)


def get_data(filename: str) -> list[int]:
    with open(filename) as f:
        raw_data = f.read()

    return [int(i) for i in raw_data.split(",")]


def solve_part_1(data):
    TOT_DAYS = 80
    fishes: list[Fish] = [Fish(i) for i in data]

    for day in range(TOT_DAYS):
        for fish in fishes:
            if fish.birthday == day and fish.timer == Fish.CHILD_INITIAL_TIMER:
                continue
            if fish.timer == 0:
                fishes.append(fish.spawn(day))
            fish.age()

    return len(fishes)


if __name__ == "__main__":
    data = get_data("input.txt")
    res1 = solve_part_1(data)
    print(f"Res 1: {res1}")
