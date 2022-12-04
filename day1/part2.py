if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        data = [int(line) for line in input_file.readlines()]
        windows = [
            data[i] + data[i + 1] + data[i + 2]
            for i, _ in enumerate(data)
            if i < len(data) - 2
        ]
        increments = 0
        for i, _ in enumerate(windows):
            if i == 0:
                continue
            if windows[i] > windows[i - 1]:
                increments += 1
        print(increments)
