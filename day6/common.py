from typing import Dict


def simulateFish(fish_counter: Dict[int, int], days: int):
    for _ in range(days):
        new_fish_counter = {i: 0 for i in range(9)}
        for timer, count in fish_counter.items():
            if timer == 0:
                new_fish_counter[6] += count
                new_fish_counter[8] += count
                continue
            new_fish_counter[timer - 1] += count
        fish_counter = new_fish_counter
    return sum(fish_counter.values())
