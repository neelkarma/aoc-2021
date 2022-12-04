if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        grid = [[int(char) for char in line.strip()] for line in input_file.readlines()]
        octopus_num = len(grid) * len(grid[0])
        step = 0
        while True:
            step += 1
            for y, row in enumerate(grid):
                for x, _ in enumerate(row):
                    grid[y][x] += 1

            curr_step_flashes = []
            queue = []
            for y, row in enumerate(grid):
                for x, energy in enumerate(row):
                    if energy > 9:
                        queue.append((x, y))

            while queue:
                x, y = queue.pop(0)
                if (x, y) in curr_step_flashes:
                    continue
                curr_step_flashes.append((x, y))
                for new_x, new_y in [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x + 1, y + 1),
                    (x - 1, y + 1),
                    (x - 1, y - 1),
                ]:
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        if not (new_x, new_y) in curr_step_flashes:
                            grid[new_y][new_x] += 1
                            if grid[new_y][new_x] > 9:
                                queue.append((new_x, new_y))
            for x, y in curr_step_flashes:
                grid[y][x] = 0

            if len(curr_step_flashes) == octopus_num:
                break
        print(step)
