# CW: Brute Forcing. Feel free to leave if you feel uncomfortable at any point.
from itertools import permutations


def all_combinations(*chars: str):
    return ["".join(comb) for comb in permutations(chars)]


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        data = [
            [side.split() for side in line.strip().split(" | ")]
            for line in input_file.readlines()
        ]
        output_sum = 0
        mapping = {
            "ab": 1,
            "abcdef": 9,
            "abcdefg": 8,
            "abcdeg": 0,
            "abcdf": 3,
            "abd": 7,
            "abef": 4,
            "acdfg": 2,
            "bcdef": 5,
            "bcdefg": 6,
        }
        for g1, g2 in data:
            for perm in permutations("abcdefg"):
                perm_map = dict(zip(perm, "abcdefg"))

                g1_list = ["".join(perm_map[c] for c in x) for x in g1]
                g2_list = ["".join(perm_map[c] for c in x) for x in g2]

                if all("".join(sorted(ans)) in mapping for ans in g1_list):
                    g2_list = ["".join(sorted(x)) for x in g2_list]
                    output_sum += int("".join(str(mapping[x]) for x in g2_list))
                    break

        print(output_sum)
