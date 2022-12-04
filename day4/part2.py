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

        is_lose = False
        last_num = -1
        unchecked_sum = -1
        lose_board = None

        for num in deck:
            for id, board in list(boards.items()):
                board.check_draw(num)
                if not board.check_win():
                    continue
                if not len(boards) == 1:
                    boards.pop(id)
                    continue
                lose_board = board
                is_lose = True
                last_num = num
                unchecked_sum = lose_board.sum_unchecked()
                break
            if is_lose:
                break

        print(last_num * unchecked_sum)
