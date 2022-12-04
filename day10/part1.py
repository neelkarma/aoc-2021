if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        open_chars = ["(", "[", "{", "<"]
        close_chars = [")", "]", "}", ">"]
        chunk_map = dict(zip(open_chars, close_chars))
        points_map = dict(zip(close_chars, [3, 57, 1197, 25137]))
        points = 0
        for line in lines:
            stack = []
            for char in line:
                if char in open_chars:
                    stack.append(char)
                if char in close_chars:
                    if chunk_map[stack[-1]] == char:
                        stack.pop()
                    else:
                        points += points_map[char]
                        break
        print(points)
