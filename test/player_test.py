import unittest

from app.player import Player
from app.player_list import PlayerList


class PlayerTest(unittest.TestCase):
    def test_player_id_and_name(self):
        player = Player("1", "HJK")
        self.assertEqual('Player ID: 1, Player Name: HJK', str(player))

    def test_player_uid_and_name_properties(self):
        player = Player("1", "HJK")
        self.assertEqual("1", player.uid)
        self.assertEqual("HJK", player.name)

    def test_insert_in_empty_list(self):
        player = Player("1", "HJK")
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty())

        player_list.insert_head(player)
        self.assertFalse(player_list.is_empty())

        self.assertEqual(player_list._head.player, player)

    def test_insert_head_in_not_empty_list(self):
        player1 = Player("1", "HJK")
        player2 = Player("2", "SSY")
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty())
        player_list.insert_head(player1)
        player_list.insert_head(player2)
        self.assertFalse(player_list.is_empty())

        self.assertEqual(player_list._head.player, player2)
        self.assertEqual(player_list._head.next.player, player1)

    def test_insert_tail_in_not_empty_list(self):
        player1 = Player("1", "HJK")
        player2 = Player("2", "SSY")
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty())
        player_list.insert_tail(player1)
        player_list.insert_tail(player2)
        self.assertFalse(player_list.is_empty())

        self.assertEqual(player_list._head.player, player1)
        self.assertEqual(player_list._tail.player, player2)
        self.assertEqual(player_list._head.next.player, player2)
        self.assertEqual(player_list._tail.previous.player, player1)

    def test_delete_from_head(self):
        player1 = Player("1", "HJK")
        player2 = Player("2", "SSY")
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty())

        player_list.insert_head(player1)
        player_list.insert_head(player2)
        self.assertFalse(player_list.is_empty())

        deleted_player = player_list.delete_head()
        self.assertEqual(deleted_player, player2)
        self.assertEqual(player_list._head.player, player1)

    def test_delete_from_tail(self):
        player1 = Player("1", "HJK")
        player2 = Player("2", "SSY")
        player3 = Player("3", "SAY")
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty())

        player_list.insert_head(player1)
        player_list.insert_tail(player2)
        player_list.insert_tail(player3)

        self.assertFalse(player_list.is_empty())

        deleted_player = player_list.delete_tail()
        self.assertEqual(deleted_player, player3)
        self.assertEqual(player_list._tail.player, player2)


if __name__ == '__main__':
    unittest.main()

