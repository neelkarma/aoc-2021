from statistics import median

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        open_chars = ["(", "[", "{", "<"]
        close_chars = [")", "]", "}", ">"]
        char_map = {k: v for k, v in zip(open_chars, close_chars)}
        incomplete_lines = []
        for line in lines:
            stack = []
            is_corrupted = False
            for char in line:
                if char in open_chars:
                    stack.append(char)
                if char in close_chars:
                    if char_map[stack[-1]] == char:
                        stack.pop()
                    else:
                        is_corrupted = True
                        break
            if not is_corrupted:
                incomplete_lines.append(line)

        points_map = {k: v for k, v in zip(close_chars, [1, 2, 3, 4])}
        scores = []
        for line in incomplete_lines:
            stack = []
            for char in line:
                if char in open_chars:
                    stack.append(char)
                if char in close_chars:
                    if char_map[stack[-1]] == char:
                        stack.pop()
            char_points = [points_map[char_map[char]] for char in reversed(stack)]
            score = 0
            for point in char_points:
                score *= 5
                score += point
            scores.append(score)
        print(median(scores))
