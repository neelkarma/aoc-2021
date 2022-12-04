# CW: Brute Forcing. Feel free to leave if you feel uncomfortable at any point.


def triangle_sum(num: int):
    return sum([i for i in range(1, num + 1)])


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        crabs = [int(crab) for crab in input_file.readline().strip().split(",")]
        lowest_fuel_cost = float("inf")
        max_distance = max(crabs)
        for i in range(0, max_distance):
            print(f"Progress: {i}/{max_distance}")
            fuel_cost = sum(triangle_sum(int(abs(i - crab))) for crab in crabs)
            if fuel_cost < lowest_fuel_cost:
                lowest_fuel_cost = fuel_cost
        print(lowest_fuel_cost)
