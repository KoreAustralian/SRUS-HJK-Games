from app.player_node import *


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        return self._head is None

    def insert_head(self, player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node

    def insert_tail(self, player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node

