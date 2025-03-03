import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_player_id_and_name(self):
        player = Player("1", "HJK")
        self.assertEqual('Player ID: 1, Player Name: HJK', str(player))

    def test_player_uid_and_name_properties(self):
        player = Player("1", "HJK")
        self.assertEqual("1", player.uid)
        self.assertEqual("HJK", player.name)


if __name__ == '__main__':
    unittest.main()

