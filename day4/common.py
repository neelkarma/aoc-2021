from typing import List


class Number:
    num: int
    checked: bool

    def __init__(self, num: int):
        self.num = num
        self.checked = False

    def check_draw(self, num: int):
        if self.num == num:
            self.checked = True
        return self.checked


class Board:
    board: List[List[Number]]

    def __init__(self, board_lines: List[str]):
        self.board = [
            [Number(int(num)) for num in row.strip().split()] for row in board_lines
        ]

    def check_draw(self, num: int):
        for row in self.board:
            for board_num in row:
                board_num.check_draw(num)

    def check_win(self):
        for i in range(5):
            if all([num.checked for num in self.board[i]]) or all(
                [num.checked for num in [self.board[j][i] for j in range(5)]]
            ):
                return True
        return False

    def sum_unchecked(self):
        sum = 0
        for row in self.board:
            for num in row:
                if not num.checked:
                    sum += num.num
        return sum
