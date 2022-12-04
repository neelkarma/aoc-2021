from typing import Dict
from enum import Enum, auto
from copy import copy


class LineOrientation(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    DIAGONAL_LEADING = auto()
    DIAGONAL_SECONDARY = auto()


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __iter__(self):
        return iter((self.x, self.y))


class Line:
    start: Point
    end: Point
    orientation: LineOrientation

    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

        if self.start.x == self.end.x:
            self.orientation = LineOrientation.VERTICAL
            if self.start.y > self.end.y:
                self.start, self.end = self.end, self.start
            return

        if self.start.y == self.end.y:
            self.orientation = LineOrientation.HORIZONTAL
            if self.start.x > self.end.x:
                self.start, self.end = self.end, self.start
            return

        if (self.start.y < self.end.y and self.start.x < self.end.x) or (
            self.end.y < self.start.y and self.end.x < self.start.x
        ):
            self.orientation = LineOrientation.DIAGONAL_LEADING
            if self.start.x > self.end.x:
                self.start, self.end = self.end, self.start
            return

        if (self.start.y > self.end.y and self.start.x < self.end.x) or (
            self.end.y > self.start.y and self.end.x < self.start.x
        ):
            self.orientation = LineOrientation.DIAGONAL_SECONDARY
            if self.start.x > self.end.x:
                self.start, self.end = self.end, self.start
            return

    def get_all_points(self):
        points = []
        iter = copy(self.start)
        points.append(copy(iter))
        match self.orientation:
            case LineOrientation.VERTICAL:
                while iter != self.end:
                    iter.y += 1
                    points.append(copy(iter))
            case LineOrientation.HORIZONTAL:
                while iter != self.end:
                    iter.x += 1
                    points.append(copy(iter))
            case LineOrientation.DIAGONAL_LEADING:
                while iter != self.end:
                    iter.x += 1
                    iter.y += 1
                    points.append(copy(iter))
            case LineOrientation.DIAGONAL_SECONDARY:
                while iter != self.end:
                    iter.x += 1
                    iter.y -= 1
                    points.append(copy(iter))
        return points


class Board:
    board: Dict[int, Dict[int, int]]

    def __init__(self) -> None:
        self.board = {}

    def process(self, line: Line):
        for x, y in line.get_all_points():
            if y not in self.board:
                self.board[y] = {x: 1}
                continue
            if x not in self.board[y]:
                self.board[y][x] = 1
                continue
            self.board[y][x] += 1

    def count_overlaps(self):
        overlaps = 0
        for row in self.board.values():
            for count in row.values():
                if count > 1:
                    overlaps += 1
        return overlaps
