from typing import Any, List, Optional, Tuple


class Point:
    def __init__(self, x: int, y: int, is_input_zero_based: bool = False):
        if is_input_zero_based:
            self._x = x
            self._y = y
        else:
            self._x = x - 1
            self._y = y - 1

    @classmethod
    def from_clue_value(cls, clue_value: str) -> 'Point':
        x = int(clue_value[0])
        y = int(clue_value[1])
        return cls(x, y)

    def get_x(self, zero_based: bool = True) -> int:
        return self._x if zero_based else self._x + 1

    def get_y(self, zero_based: bool = True) -> int:
        return self._y if zero_based else self._y + 1

    def coords(self, zero_based: bool = True) -> Tuple[int, int]:
        return self.get_x(zero_based=zero_based), self.get_y(zero_based=zero_based)

    def __str__(self) -> str:
        x, y = self.coords(zero_based=False)
        return f'{x}{y}'

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Point):
            return self.get_x() == other.get_x() and self.get_y() == other.get_y()
        return False

    def __hash__(self) -> int:
        return hash((self.get_x(), self.get_y()))


class Clue:
    def __init__(self, clue_point: Point, clue_value: str):
        self._point = clue_point
        self._value = clue_value

    def get_next_clue_point(self) -> Point:
        return Point.from_clue_value(self._value)

    def is_treasure(self) -> bool:
        return self._point == self.get_next_clue_point()

    def get_value_as_int(self) -> int:
        return int(self._value)


class TreasureSeek:
    def __init__(self, tmap: List[List[str]]):
        self.__tmap = tmap

    def __get_clue(self, clue_point: Point) -> Clue:
        x, y = clue_point.coords()
        clue_value = self.__tmap[x][y]
        return Clue(clue_point, clue_value)

    def find_treasure(self, start_x: int = 1, start_y: int = 1) -> Optional[int]:
        p = Point(x=start_x, y=start_y)
        log_message = f'{p}'
        clue = self.__get_clue(p)
        points_history = set()
        while not clue.is_treasure():
            if p in points_history:
                log_message = (
                    f'{log_message}...\n'
                    f'There is no such treasure in the given map, which can be found by clues. [clues are looped]'
                )
                print(log_message)
                return None
            points_history.add(p)
            p = clue.get_next_clue_point()
            log_message = f'{log_message}, {p}'
            clue = self.__get_clue(p)
        else:
            print(log_message)
            return clue.get_value_as_int()
