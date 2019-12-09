from unittest import TestCase

from functional_recursive import TreasureSeek


class TestRecursive(TestCase):
    def test_treasure_seek__example_treasure_map(self):
        tmap = [
            ['55', '14', '25', '52', '21', ],
            ['44', '31', '11', '53', '43', ],
            ['24', '13', '45', '12', '34', ],
            ['42', '22', '43', '32', '41', ],
            ['51', '23', '33', '54', '15', ],
        ]
        ts = TreasureSeek(tmap)
        treasure = ts.find_treasure()
        expected_treasure = 43
        self.assertEqual(treasure, expected_treasure)

    def test_treasure_seek__infinite_case_one(self):
        tmap = [
            ['55', '14', '25', '52', '21', ],
            ['44', '31', '11', '53', '43', ],
            ['24', '13', '45', '12', '34', ],
            ['42', '22', '43', '32', '41', ],
            ['51', '23', '33', '54', '11', ],
        ]
        ts = TreasureSeek(tmap)
        treasure = ts.find_treasure()
        self.assertIsNone(treasure)

    def test_treasure_seek__infinite_case_two(self):
        tmap = [
            ['55', '14', '25', '52', '21', ],
            ['44', '31', '11', '53', '43', ],
            ['24', '13', '45', '12', '34', ],
            ['42', '22', '24', '32', '41', ],
            ['51', '23', '33', '54', '15', ],
        ]
        ts = TreasureSeek(tmap)
        treasure = ts.find_treasure()
        self.assertIsNone(treasure)
