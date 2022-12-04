from pprint import pprint
from collections import Counter, defaultdict

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        template = lines.pop(0)

        # Create and populate template dictionary
        template_dict = defaultdict(lambda: 0)
        for i in range(len(template) - 1):
            template_dict[template[i : i + 2]] += 1

        # Get pair rules
        lines.pop(0)
        pair_rules = {
            el_pair: added_el
            for el_pair, added_el in iter(line.split(" -> ") for line in lines)
        }

        for _ in range(10):
            for matcher, result in pair_rules.items():
                if template_dict[matcher] > 0:
                    template_dict[matcher[0] + result] += template_dict[matcher]
                    template_dict[result + matcher[1]] += template_dict[matcher]
                    template_dict[matcher] = 0
        pprint(template_dict)
        char_counter = dict(Counter("".join(k * v for k, v in template_dict.items())))
        pprint(char_counter)
        print(max(char_counter.values()) - min(char_counter.values()))
