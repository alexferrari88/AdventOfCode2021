from typing import Any
import numpy as np

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


def mark_card(
    card: list[list[int]], marked_card: np.ndarray, drawn_number: int
) -> tuple[np.ndarray, bool]:
    is_num_in_card = False
    for row_index, row in enumerate(card):
        for col_index, card_num in enumerate(row):
            if card_num == drawn_number:
                is_num_in_card = True
                marked_card[row_index, col_index] = 1
                return (marked_card, is_num_in_card)

    return (marked_card, is_num_in_card)


def check_card_for_win(marked_card: np.ndarray) -> bool:
    rows_sum = np.sum(marked_card, axis=1)
    cols_sum = np.sum(marked_card, axis=0)
    if BINGO_ROW_COLUMN_SIZE in rows_sum or BINGO_ROW_COLUMN_SIZE in cols_sum:
        return True

    return False


def flatten_list(t: list[list[Any]]) -> list[Any]:
    return [item for sublist in t for item in sublist]


def solve_part_1(cards, numbers):
    marked_cards = [
        np.zeros((BINGO_ROW_COLUMN_SIZE, BINGO_ROW_COLUMN_SIZE), dtype=np.uintc)
        for _ in range(len(cards))
    ]
    nums_checked_in_cards = [set() for i in range(len(cards))]
    for n in numbers:
        for card_index, card in enumerate(cards):
            all_nums_in_card = set(flatten_list(card))
            marked_card, is_num_in_card = mark_card(
                card=card, marked_card=marked_cards[card_index], drawn_number=n
            )
            marked_cards[card_index] = marked_card
            if is_num_in_card:
                nums_checked_in_cards[card_index].add(n)
            if check_card_for_win(marked_card):
                unused_nums = all_nums_in_card.difference(
                    nums_checked_in_cards[card_index]
                )
                return sum(unused_nums) * n


if __name__ == "__main__":
    data = get_data("input.txt")
    cards, drawn_numbers = process_data(data)
    res1 = solve_part_1(cards, drawn_numbers)
    print(f"Res 1: {res1}")
