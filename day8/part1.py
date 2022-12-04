if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        data = [
            [side.split() for side in line.strip().split(" | ")]
            for line in input_file.readlines()
        ]
        unique_count = 0
        for line in data:
            for display in line[1]:
                if len(display) in [2, 4, 3, 7]:
                    unique_count += 1
        print(unique_count)
