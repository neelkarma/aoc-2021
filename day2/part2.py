if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        instructions = [line.split() for line in input_file.readlines()]
        x = 0
        d = 0
        aim = 0
        for direction, amount in instructions:
            amount = int(amount)
            match direction:
                case "forward":
                    x += amount
                    d += aim * amount
                case "down":
                    aim += amount
                case "up":
                    aim -= amount
        print(x * d)
