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

