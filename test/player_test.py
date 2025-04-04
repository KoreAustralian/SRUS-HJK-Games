import unittest
import random


from app.player import Player
from app.player_list import PlayerList


class PlayerTest(unittest.TestCase):
    # def test_player_id_and_name(self):
    #     player = Player("1", "HJK")
    #     self.assertEqual('Player ID: 1, Player Name: HJK', str(player))
    #
    # def test_player_uid_and_name_properties(self):
    #     player = Player("1", "HJK")
    #     self.assertEqual("1", player.uid)
    #     self.assertEqual("HJK", player.name)
    #
    # def test_insert_in_empty_list(self):
    #     player = Player("1", "HJK")
    #     player_list = PlayerList()
    #     self.assertTrue(player_list.is_empty())
    #
    #     player_list.insert_head(player)
    #     self.assertFalse(player_list.is_empty())
    #
    #     self.assertEqual(player_list._head.player, player)
    #
    # def test_insert_head_in_not_empty_list(self):
    #     player1 = Player("1", "HJK")
    #     player2 = Player("2", "SSY")
    #     player_list = PlayerList()
    #
    #     self.assertTrue(player_list.is_empty())
    #     player_list.insert_head(player1)
    #     player_list.insert_head(player2)
    #     self.assertFalse(player_list.is_empty())
    #
    #     self.assertEqual(player_list._head.player, player2)
    #     self.assertEqual(player_list._head.next.player, player1)
    #
    # def test_insert_tail_in_not_empty_list(self):
    #     player1 = Player("1", "HJK")
    #     player2 = Player("2", "SSY")
    #     player_list = PlayerList()
    #
    #     self.assertTrue(player_list.is_empty())
    #     player_list.insert_tail(player1)
    #     player_list.insert_tail(player2)
    #     self.assertFalse(player_list.is_empty())
    #
    #     self.assertEqual(player_list._head.player, player1)
    #     self.assertEqual(player_list._tail.player, player2)
    #     self.assertEqual(player_list._head.next.player, player2)
    #     self.assertEqual(player_list._tail.previous.player, player1)
    #
    # def test_delete_from_head(self):
    #     player1 = Player("1", "HJK")
    #     player2 = Player("2", "SSY")
    #     player_list = PlayerList()
    #     self.assertTrue(player_list.is_empty())
    #
    #     player_list.insert_head(player1)
    #     player_list.insert_head(player2)
    #     self.assertFalse(player_list.is_empty())
    #
    #     deleted_player = player_list.delete_head()
    #     self.assertEqual(deleted_player, player2)
    #     self.assertEqual(player_list._head.player, player1)
    #
    # def test_delete_from_tail(self):
    #     player1 = Player("1", "HJK")
    #     player2 = Player("2", "SSY")
    #     player3 = Player("3", "SAY")
    #     player_list = PlayerList()
    #     self.assertTrue(player_list.is_empty())
    #
    #     player_list.insert_head(player1)
    #     player_list.insert_tail(player2)
    #     player_list.insert_tail(player3)
    #
    #     self.assertFalse(player_list.is_empty())
    #
    #     deleted_player = player_list.delete_tail()
    #     self.assertEqual(deleted_player, player3)
    #     self.assertEqual(player_list._tail.player, player2)
    #
    # def test_delete_middle_node_by_key(self):
    #     player1 = Player("1", "HJK")
    #     player2 = Player("2", "SSY")
    #     player3 = Player("3", "SAY")
    #     player_list = PlayerList()
    #
    #     player_list.insert_head(player1)
    #     player_list.insert_tail(player2)
    #     player_list.insert_tail(player3)
    #
    #     deleted_player = player_list.delete_by_key("2")
    #     self.assertEqual(deleted_player, player2)
    #     self.assertEqual(player_list._head.player, player1)
    #     self.assertEqual(player_list._tail.player, player3)
    #     self.assertEqual(player_list._head.next.player, player3)
    #     self.assertEqual(player_list._tail.previous.player, player1)

    def test_sort_players(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03', "Charlie", 15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02', "Bob", 5), Player('01', "Alice", 10),
                                    Player('03', "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player('01', "Alice", 10)
        bob = Player('02', "Bob", 5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)

    def test_sort_player_descending(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03', "Charlie", 15)]

        sorted_players = Player.sort_descending(players)

        manually_sorted_players = [Player('02', "Bob", 5), Player('01', "Alice", 10), Player('03', "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def tes_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", random.randint(0, 1000)) for i in range(1000)]

        sorted_players = Player.sort_descending(players)

        for i in range(sorted_players):
            self.assertTrue(sorted_players[i].score < sorted_players[i+1].score)


if __name__ == '__main__':
    unittest.main()

