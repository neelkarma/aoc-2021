import itertools
from common import Board


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        deck = [int(num) for num in lines.pop(0).split(",")]
        lines.pop(0)
        boards = {
            id: Board(list(board))
            for id, (is_blank, board) in enumerate(
                itertools.groupby(lines, lambda x: x == "")
            )
            if not is_blank
        }

        is_win = False
        last_num = -1
        unchecked_sum = -1
        win_board = None
        for num in deck:
            for id, board in list(boards.items()):
                board.check_draw(num)
                if not board.check_win():
                    continue
                win_board = board
                last_num = num
                is_win = True
                unchecked_sum = win_board.sum_unchecked()
                break
            if is_win:
                break

        print(last_num * unchecked_sum)
