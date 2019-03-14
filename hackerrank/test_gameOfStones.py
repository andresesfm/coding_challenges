import unittest
import gameOfStones


class TestGameOfStones(unittest.TestCase):

    def test_gos1(self):
        self.assertEqual(gameOfStones.gameOfStones(1), "Second")

    def test_gos2(self):
        self.assertEqual(gameOfStones.gameOfStones(2), "First")

if __name__ == '__main__':
    unittest.main()