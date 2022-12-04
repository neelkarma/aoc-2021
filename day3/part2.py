from typing import List
from common import bit_count


def calculate_oxygen(diagnostics: List[str]):
    for i, _ in enumerate(diagnostics[0]):
        if len(diagnostics) == 1:
            break
        ones, zeroes = bit_count(diagnostics, i)
        filter_value = "1" if ones >= zeroes else "0"
        diagnostics = [line for line in diagnostics if line[i] == filter_value]
    return diagnostics[0]


def calculate_carbon(diagnostics: List[str]):
    for i, _ in enumerate(diagnostics[0]):
        if len(diagnostics) == 1:
            break
        ones, zeroes = bit_count(diagnostics, i)
        filter_value = "0" if zeroes <= ones else "1"
        diagnostics = [line for line in diagnostics if line[i] == filter_value]
    return diagnostics[0]


if __name__ == "__main__":
    with open("./input.txt", "r") as inputFile:
        diagnostics = [line.strip() for line in inputFile.readlines()]
        oxygen = int(calculate_oxygen(diagnostics), 2)
        carbon = int(calculate_carbon(diagnostics), 2)
        print(oxygen * carbon)
