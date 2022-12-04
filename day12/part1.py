from pprint import pprint
from collections import defaultdict

if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        lines = [
            [location for location in line.strip().split("-")]
            for line in input_file.readlines()
        ]
        graph = defaultdict(list)
        for pos1, pos2 in lines:
            graph[pos1].append(pos2)
            graph[pos2].append(pos1)

        def dfs(curr_cave, path=None):
            if path is None:
                path = []

            path.append(curr_cave)

            if curr_cave == "end":
                print(path)

            for next_cave in graph[curr_cave]:
                if next_cave not in path:
                    dfs(next_cave, path)

        pprint(dict(graph))
        print("")
        dfs("start")
