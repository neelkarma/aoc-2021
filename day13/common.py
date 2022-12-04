from enum import Enum, auto
import re


class Axis(Enum):
    X = auto()
    Y = auto()


axis_map = {"x": Axis.X, "y": Axis.Y}
fold_regex = re.compile(r"^fold along ([xy])=(\d+)$")
