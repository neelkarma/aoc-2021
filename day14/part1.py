from collections import Counter

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        input_file.seek(0)
        lines = [line.strip() for line in input_file.readlines()]
        template = lines.pop(0)
        lines.pop(0)
        pair_rules = {
            el_pair: added_el
            for el_pair, added_el in iter(line.split(" -> ") for line in lines)
        }
        for _ in range(10):
            pointer = 0
            while pointer < len(template):
                slice = template[pointer : pointer + 2]
                if slice in pair_rules:
                    template = (
                        template[: pointer + 1]
                        + pair_rules[slice]
                        + template[pointer + 1 :]
                    )
                    pointer += 1
                pointer += 1
        char_counter = dict(Counter(template))
        print(max(char_counter.values()) - min(char_counter.values()))
