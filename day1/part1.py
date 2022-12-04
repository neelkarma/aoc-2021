if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        data = [int(line) for line in input_file.readlines()]
        increments = 0
        for i, _ in enumerate(data[1:]):
            if data[i] > data[i - 1]:
                increments += 1
        print(increments)
