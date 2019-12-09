#!/usr/bin/python3
from common import get_treasure_map_from_stdin, get_treasure_map_example
from functional_recursive import TreasureSeek as RecursiveTreasureSeek
from oop_nonrecursive import TreasureSeek as NonRecursiveTreasureSeek


def main(use_example_map: bool = False):
    if use_example_map:
        treasure_map = get_treasure_map_example()
    else:
        treasure_map = get_treasure_map_from_stdin()

    print('\n\n~Non-Recursive~')
    t = NonRecursiveTreasureSeek(treasure_map)
    print(f'Last Clue: {t.find_treasure()}')
    print('\n\n~Recursive~')
    t = RecursiveTreasureSeek(treasure_map)
    print(f'Last Clue: {t.find_treasure()}')


if __name__ == '__main__':
    main(use_example_map=False)
    print("\n\nI'm done")
