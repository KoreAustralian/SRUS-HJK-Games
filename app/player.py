class Player:
    def __init__(self, uid, player_name, score):
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

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f'Player ID: {self._uid}, Player Name: {self._player_name}, Player Score: {self._score}'

    def __hash__(self):
        return Player.hash_function(self._uid)

    def __eq__(self, other):
        return self._uid == other.uid

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.uid!r}, "

    @score.setter
    def score(self, value):
        if isinstance(value, int) and value >= 0:
            self._score = value
        else:
            raise ValueError("It is non-positive value.")

    @classmethod
    def hash_function(cls, key: str) -> int:
        return sum(ord(char) for char in key)

    @classmethod
    def sort_descending(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
        return cls.sort_descending(left) + [pivot] + cls.sort_descending(right)



