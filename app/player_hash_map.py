from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:
    SIZE = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash_function(key) % self.SIZE

    def __setitem__(self, key: str, name: str):
        index = self.get_index(key)
        player_list = self.hashmap[index]

        # Check if the player is already on that player list.
        current = player_list.head
        while current:
            if current.key == key:
                # If it is, update the player's name.
                current.player._player_name = name
                return
            current = current.next

        # If it isn't, create a player and add the player to the player list.
        new_player = Player(key, name)
        player_list.insert_tail(new_player)

    def __getitem__(self, key: str) -> Player | None:
        index = self.get_index(key)
        player_list = self.hashmap[index]

        current = player_list.head
        while current:
            if current.key == key:
                return current.player
            current = current.next

        return None

    def __delitem__(self, key: str) -> None:
        index = self.get_index(key)
        player_list = self.hashmap[index]

        deleted_player = player_list.delete_by_key(key)
        if deleted_player is None:
            print(f" cannot find {key}")

    def display(self):
        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty():
                continue

            print(f"{index})", end="")

            current = player_list.head
            while current:
                print(current.player, end="")

                if current.next:
                    print(" -> ", end="")
                current = current.next

            print()


