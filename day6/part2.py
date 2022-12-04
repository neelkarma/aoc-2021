from common import simulateFish

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        fishes = [int(timer) for timer in input_file.readline().strip().split(",")]
        fish_counter = {i: fishes.count(i) for i in range(9)}
        print(simulateFish(fish_counter, 256))
