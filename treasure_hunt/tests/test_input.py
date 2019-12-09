from unittest import TestCase

from common import _get_clues_from_input_line


class TestInput(TestCase):
    def test_get_clues_from_input_line__empty_line(self):
        input_line = ''
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__five_empty_clues(self):
        input_line = ',,,,'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__four_valid_clues(self):
        input_line = '11,12,13,14'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__six_valid_clues(self):
        input_line = '11,12,13,14,15,21'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__four_valid_clues_one_invalid_nondigit_clue(self):
        input_line = '11,12,13,ab,14'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__four_valid_clues_one_invalid_outofrangedigit_clue(self):
        input_line = '11,12,13,61,15'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__four_valid_clues_one_invalid_onedigit_clue(self):
        input_line = '11,12,13,14,5'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__four_valid_clues_one_invalid_threedigit_clue(self):
        input_line = '12,13,15,14,111'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = []
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__five_valid_clues_without_whitespaces(self):
        input_line = '11,12,13,14,15'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = ['11', '12', '13', '14', '15']
        self.assertListEqual(clues, expected_clues)

    def test_get_clues_from_input_line__five_valid_clues_with_whitespaces(self):
        input_line = '11\t,  12,13  ,14,\t15'
        clues, _ = _get_clues_from_input_line(input_line)
        expected_clues = ['11', '12', '13', '14', '15']
        self.assertListEqual(clues, expected_clues)
