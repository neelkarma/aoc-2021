if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        grid = [
            [int(point) for point in line]
            for line in [line.strip() for line in input_file.readlines()]
        ]
        total_risk = 0
        for y, rows in enumerate(grid):
            for x, point in enumerate(rows):
                if (
                    (point < grid[y + 1][x] if y + 1 < len(grid) else True)
                    and (point < grid[y - 1][x] if y - 1 >= 0 else True)
                    and (point < grid[y][x + 1] if x + 1 < len(rows) else True)
                    and (point < grid[y][x - 1] if x - 1 >= 0 else True)
                ):
                    total_risk += point + 1
        print(total_risk)
