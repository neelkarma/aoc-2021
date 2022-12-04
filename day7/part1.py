from statistics import median

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        crabs = [int(crab) for crab in input_file.readline().strip().split(",")]
        median_pos = median(crabs)
        print(sum(abs(median_pos - crab) for crab in crabs))
