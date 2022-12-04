from common import Axis, axis_map, fold_regex


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        # Interpret data
        points_raw, folds_raw = input_file.read().split("\n\n")
        points = set(
            tuple(int(coord) for coord in coords.split(","))
            for coords in points_raw.split("\n")
        )
        folds = []
        for line in folds_raw.split("\n"):
            match = fold_regex.match(line)
            if not match:
                raise ValueError(f"Invalid fold instruction: {line}")
            folds.append((axis_map[match.group(1)], int(match.group(2))))

        # Compute fold
        fold_axis, fold_at = folds[0]
        for x, y in points.copy():
            match fold_axis:
                case Axis.X:
                    if x > fold_at:
                        new_point = (fold_at - abs(fold_at - x), y)
                        points.remove((x, y))
                        points.add(new_point)
                case Axis.Y:
                    if y > fold_at:
                        new_point = (x, fold_at - abs(fold_at - x))
                        points.remove((x, y))
                        points.add(new_point)
        print(len(points))
