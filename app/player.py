class Player:
    def __init__(self, uid: str, player_name: str):
        self._uid = uid
        self._player_name = player_name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._player_name

    def __str__(self):
        return f'Player ID: {self._uid}, Player Name: {self._player_name}'

    def __hash__(self):
        return Player.hash_function(self._uid)

    def __eq__(self, other):
        return self._uid == other.uid

    @classmethod
    def hash_function(cls, key: str) -> int:
        return sum(ord(char) for char in key)


