import unittest

from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):

    def test_setitem(self):
        phm = PlayerHashMap()
        phm["1"] = "HJK"
        player = phm["1"]
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "HJK")

    def test_update_existing_player(self):
        phm = PlayerHashMap()
        phm["1"] = "HJK"
        phm["1"] = "SSY"
        player = phm["1"]
        self.assertEqual(player.name, "SSY")

    def test_delete_player(self):
        phm = PlayerHashMap()
        phm["1"] = "HJK"
        phm["2"] = "SSY"

        del phm["1"]
        deleted = phm["1"]
        remaining = phm["2"]

        self.assertIsNone(deleted)

        self.assertIsNotNone(remaining)
        self.assertEqual(remaining.name, "SSY")

    def test_collision_handling(self):
        phm = PlayerHashMap()
        uid1 = "a1"
        uid2 = "b1"

        phm[uid1] = "Player A"
        phm[uid2] = "Player B"

        player_a = phm[uid1]
        player_b = phm[uid2]

        self.assertEqual(player_a.name, "Player A")
        self.assertEqual(player_b.name, "Player B")


if __name__ == '__main__':
    unittest.main()
