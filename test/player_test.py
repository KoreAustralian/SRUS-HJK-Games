import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_player_id_and_name(self):
        player = Player("1", "HJK")
        self.assertEqual('Player ID: 1, Player Name: HJK', str(player))

    def test_player_id_with_special_chars(self):
        player = Player("#0123", "HJK")
        self.assertEqual('Player ID: #0123, Player Name: HJK', str(player))


if __name__ == '__main__':
    unittest.main()

