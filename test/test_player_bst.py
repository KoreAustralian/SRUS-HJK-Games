import unittest

from app.player_bst import PlayerBst
from app.player_bnode import PlayerBnode


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class TestPlayerBst(unittest.TestCase):
    def test_insert_new_node(self):
        bst = PlayerBst()
        player = Player("hongjae", 100)
        bst.insert(player)
        root = bst.root
        self.assertIsNotNone(root)
        self.assertEqual(root.player.name, "hongjae")
        self.assertEqual(root.player.score, 100)

    def test_insert_left_node(self):
        bst = PlayerBst()
        bst.insert(Player("suyeon", 200))
        bst.insert(Player("hongjae", 100))
        self.assertEqual(bst.root.left.player.name, "hongjae")
        self.assertEqual(bst.root.left.player.score, 100)

    def test_insert_right_node(self):
        bst = PlayerBst()
        bst.insert(Player("hongjae", 100))
        bst.insert(Player("suyeon", 200))
        self.assertEqual(bst.root.right.player.name, "suyeon")
        self.assertEqual(bst.root.right.player.score, 200)

    def test_search_existing_node(self):
        bst = PlayerBst()
        bst.insert(Player("suyeon", 200))
        bst.insert(Player("hongjae", 100))

        node = bst.search("hongjae")
        self.assertIsNotNone(node)
        self.assertEqual(node.player.name, "hongjae")
        self.assertEqual(node.player.score, 100)

        node = bst.search("suyeon")
        self.assertIsNotNone(node)
        self.assertEqual(node.player.name, "suyeon")
        self.assertEqual(node.player.score, 200)

    def test_search_from_empty(self):
        bst = PlayerBst()
        node = bst.search("AnyName")
        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()