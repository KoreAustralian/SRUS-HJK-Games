class Player:
    def __init__(self, uid: str, player_name: str, score: int) -> None:
        self._uid = uid
        self._player_name = player_name
        self._score = score

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f'Player ID: {self._uid}, Player Name: {self._player_name}, Player Score: {self._score}'

    def __hash__(self):
        return Player.hash_function(self._uid)

    def __eq__(self, other):
        return self._uid == other.uid

    @score.setter
    def score(self, value):
        if isinstance(value, int) and valur >= 0:
            self._score = value
        else:
            raise ValueError("It is non-positive interger.")

    @classmethod
    def hash_function(cls, key: str) -> int:
        return sum(ord(char) for char in key)


