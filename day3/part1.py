from common import bit_count

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        diagnostics = [line.strip() for line in input_file.readlines()]
        gamma_bin = ""

        for i, _ in enumerate(diagnostics[0]):
            ones, zeroes = bit_count(diagnostics, i)
            gamma_bin += "1" if ones > zeroes else "0"

        epsilon_bin = "".join(["0" if bit == "1" else "1" for bit in gamma_bin])

        gamma = int(gamma_bin, 2)
        epsilon = int(epsilon_bin, 2)
        print(gamma * epsilon)
