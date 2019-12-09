from typing import List, Optional, Tuple


class TreasureSeek:
    def __init__(self, tmap: List[List[str]]):
        self._tmap = tmap

    def __get_clue_value(self, clue_point: Tuple[int, int]):
        x, y = clue_point
        return self._tmap[x - 1][y - 1]

    @staticmethod
    def __is_treasure(clue_point: Tuple[int, int], clue_value: str) -> bool:
        x, y = clue_point
        return int(clue_value[0]) == x and int(clue_value[1]) == y

    @staticmethod
    def __get_next_clue_point(clue_value: str) -> Tuple[int, int]:
        return int(clue_value[0]), int(clue_value[1])

    def __find_treasure_recursively(
            self, clue_point: Tuple[int, int], clue_value: str, points_history: set, log_message: str
    ) -> Optional[int]:
        if self.__is_treasure(clue_point, clue_value):
            print(log_message)
            return int(clue_value)
        elif clue_point in points_history:
            log_message = (
                f'{log_message}...\n'
                f'There is no such treasure in the given map, which can be found by clues. [clues are looped]'
            )
            print(log_message)
            return None
        else:
            points_history.add(clue_point)
            clue_point = self.__get_next_clue_point(clue_value)
            log_message = f'{log_message}, {clue_point[0]}{clue_point[1]}'
            clue_value = self.__get_clue_value(clue_point)
            return self.__find_treasure_recursively(
                clue_point=clue_point, clue_value=clue_value, points_history=points_history, log_message=log_message
            )

    def find_treasure(self, start_x: int = 1, start_y: int = 1) -> Optional[int]:
        clue_point = (start_x, start_y)
        clue_value = self.__get_clue_value(clue_point)
        return self.__find_treasure_recursively(
            clue_point=clue_point, clue_value=clue_value,
            points_history=set(), log_message=f'{clue_point[0]}{clue_point[1]}'
        )
