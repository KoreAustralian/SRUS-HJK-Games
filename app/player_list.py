from app.player_node import *
from app.player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

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
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.previous = None

        return deleted_node.player

    def delete_tail(self):
        if self.is_empty():
            return None

        deleted_node = self._tail

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
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

    def display(self, forward=True):
        if self.is_empty():
            print("list is empty")
            return

        if forward:
            current = self._head
            while current:
                print(current.player)
                current = current.next
        else:
            current = self.tail
            while current:
                print(current.player)
                current = current.previous


# # checking display code
# players = PlayerList()
# player1 = Player("1", "HJK")
# player2 = Player("2", "SSY")
# player3 = Player("3", "SAY")
#
# players.insert_head(player1)
# players.insert_tail(player2)
# players.insert_tail(player3)
#
# print("Print Items in the Doubly linked forwards:")
# players.display()
#
# print("Print Items in the Doubly linked backwards:")
# players.display(forward=False)
