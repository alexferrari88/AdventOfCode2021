import re

BINGO_ROW_COLUMN_SIZE = 5


def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        data = file.readlines()
    return data


def convert_row_to_int_list(row: str) -> list[int]:
    to_return: list[int] = []
    for i in range(0, len(row), 3):
        digits = int(row[i : i + 2].strip())
        to_return.append(digits)
    return to_return


def process_raw_card(card: list[str]) -> list[int]:
    for i, row in enumerate(card):
        row = row.strip()
        card[i] = convert_row_to_int_list(row)
    return card


def process_data(data: list[str]) -> tuple[list[list[int]], list[int]]:
    drawn_numbers = [int(i.strip()) for i in data.pop(0).split(",")]
    cards = []
    for i in range(0, len(data), BINGO_ROW_COLUMN_SIZE + 1):
        card = process_raw_card(data[i + 1 : i + BINGO_ROW_COLUMN_SIZE + 1])
        cards.append(card)

    return (cards, drawn_numbers)


if __name__ == "__main__":
    data = get_data("input.txt")
    cards, drawn_numbers = process_data(data)
