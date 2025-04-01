import unittest
import sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'app')))

from app.player import *
from app.player_list import *


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

    def test_delete_middle_node_by_key(self):
        player1 = Player("1", "HJK")
        player2 = Player("2", "SSY")
        player3 = Player("3", "SAY")
        player_list = PlayerList()

        player_list.insert_head(player1)
        player_list.insert_tail(player2)
        player_list.insert_tail(player3)

        deleted_player = player_list.delete_by_key("2")
        self.assertEqual(deleted_player, player2)
        self.assertEqual(player_list._head.player, player1)
        self.assertEqual(player_list._tail.player, player3)
        self.assertEqual(player_list._head.next.player, player3)
        self.assertEqual(player_list._tail.previous.player, player1)

    def test_sort_players(self):
        players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5), Player("Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players == [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10),
                                    Player("Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)


if __name__ == '__main__':
    unittest.main()

