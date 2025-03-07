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

    def delete_head(self):
        if self.is_empty():
            return None

        deleted_node = self._head
        self._head = self._head.next
        self._head.previous = None

        return deleted_node.player

    def delete_tail(self):
        if self.is_empty():
            return None

        deleted_node = self._tail
        self._tail = self._tail.previous
        self._tail.next = None

        return deleted_node.player

    def delete_by_key(self, key):
        if self.is_empty():
            return None

        current = self._head

        while current:
            if current.key == key:
                if current == self._head:
                    return self.delete_head()
                elif current == self._tail:
                    return self.delete_tail()
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return current.player
            current = current.next
        return None

