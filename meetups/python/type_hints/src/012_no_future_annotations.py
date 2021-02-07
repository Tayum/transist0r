from typing import Tuple


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, val: Tuple[int, int]) -> "Point":
        return Point(x=val[0], y=val[1])
