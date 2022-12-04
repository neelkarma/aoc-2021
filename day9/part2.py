from numpy import prod

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        grid = [
            [int(point) for point in line]
            for line in [line.strip() for line in input_file.readlines()]
        ]
        risks = []
        for y, rows in enumerate(grid):
            for x, point in enumerate(rows):
                if (
                    (point < grid[y + 1][x] if y + 1 < len(grid) else True)
                    and (point < grid[y - 1][x] if y - 1 >= 0 else True)
                    and (point < grid[y][x + 1] if x + 1 < len(rows) else True)
                    and (point < grid[y][x - 1] if x - 1 >= 0 else True)
                ):
                    risks.append((x, y))

        basin_sizes = []
        for risk in risks:
            checked_points = []
            queue = [risk]
            while queue:
                x, y = queue.pop(0)
                if (x, y) in checked_points:
                    continue
                if x + 1 < len(grid[0]):
                    if grid[y][x + 1] != 9:
                        queue.append((x + 1, y))
                if x - 1 >= 0:
                    if grid[y][x - 1] != 9:
                        queue.append((x - 1, y))
                if y + 1 < len(grid):
                    if grid[y + 1][x] != 9:
                        queue.append((x, y + 1))
                if y - 1 >= 0:
                    if grid[y - 1][x] != 9:
                        queue.append((x, y - 1))
                checked_points.append((x, y))
            basin_sizes.append(len(checked_points))
        print(prod(sorted(basin_sizes, reverse=True)[:3]))
