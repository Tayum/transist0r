from typing import List, Tuple


def _get_clues_from_input_line(input_line: str) -> Tuple[List[str], str]:
    clues = []

    input_line = input_line.strip()
    parsed_clues = [clue.strip() for clue in input_line.split(',')]

    def is_clue_valid(clue):
        return len(clue) == 2 and all('1' <= char <= '5' for char in clue)

    if len(parsed_clues) != 5:
        log_msg = f'Expected 5 clues to be inputted, got {len(parsed_clues)}.'
    elif not all(is_clue_valid(clue) for clue in parsed_clues):
        log_msg = (
            'Some inputted clues are invalid! Remember that clue should consist of exactly two digits, '
            'each laying in a range of 1 to 5, representing the row and the column respectively.'
        )
    else:
        clues = parsed_clues
        log_msg = 'Input line received successfully.'

    return clues, log_msg


def get_treasure_map_from_stdin() -> List[List[str]]:
    tmap = []
    while len(tmap) != 5:
        input_line = input(f'Please enter the 5 clues for #{len(tmap) + 1} row, separating them with comma (","): ')
        clues, log_msg = _get_clues_from_input_line(input_line)
        print(log_msg)
        if clues:
            tmap.append(clues)

    return tmap


def get_treasure_map_example() -> List[List[str]]:
    return [
        ['55', '14', '25', '52', '21', ],
        ['44', '31', '11', '53', '43', ],
        ['24', '13', '45', '12', '34', ],
        ['42', '22', '43', '32', '41', ],
        ['51', '23', '33', '54', '15', ],
    ]
