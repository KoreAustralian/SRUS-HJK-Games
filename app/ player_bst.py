from app.player_bnode import PlayerBNode


class PlayerBst:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        """ Insert new Player object into the binary seach tree based on the player's name """
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

    def search(self, name):
        """ Search Player node by name """
        return self._search_recursive(self._root, name)

    def _search_recursive(self, current_node, name):
        if current_node is None:
            return None
        if current_node.player.name == name:
            return current_node
        elif name < current_node.player.name:
            return self._search_recursive(current_node.left, name)
        else:
            return self._search_recursive(current_node.right, name)

    def to_sorted_list(self):
        """Return a sorted list"""
        sorted_list = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            sorted_list.append(node)
            inorder(node.right)

        inorder(self._root)
        return sorted_list

    def _build_balanced_bst(self, nodes_list):
        """Build a balanced BST from sorted nodes list"""
        if not nodes_list:
            return None
        mid_index = len(nodes_list) // 2
        middle_node = nodes_list[mid_index]

        # Create a new node (or reuse existing node if preferred)
        new_node = PlayerBNode(middle_node.player)

        # Recursively build left and right subtrees
        new_node.left = self._build_balanced_bst(nodes_list[:mid_index])
        new_node.right = self._build_balanced_bst(nodes_list[mid_index + 1:])

        return new_node

    def balance(self):
        """Balance the BST"""
        nodes_list = self.to_sorted_list()
        self._root = self._build_balanced_bst(nodes_list)

