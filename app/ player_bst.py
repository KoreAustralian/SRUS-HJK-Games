from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        # Insert new Player object into the binary seach tree based on the player's name.
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self.insert_recursive(self._root, player)

    def insert_recursive(self, current_node, player):
        key = player.name
        current_key = current_node.player.name

        if key == current_key:
            current_node.player = player
        elif key < current_key:
            # Insert into the left subtree
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self.insert_recursive(current_node.left, player)
        else:
            # Insert into the right subtree
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self.insert_recursive(current_node.right, player)
