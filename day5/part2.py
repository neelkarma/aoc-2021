from common import Line, Point, Board


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        lines = [
            Line(
                *[
                    Point(*[int(coord) for coord in coords.split(",")])
                    for coords in line.split(" -> ")
                ]
            )
            for line in input_file.readlines()
        ]

        board = Board()

        for line in lines:
            board.process(line)

        print(board.count_overlaps())
