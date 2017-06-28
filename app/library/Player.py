import uuid

class Player:
    __player_map = {}

    @staticmethod
    def get_all():
        return Player.__player_map.values()

    @staticmethod
    def get_by_id(id):
        return Player.__player_map[id]

    def __init__(self, name, game_key, sid):
        self.id = str(uuid.uuid1())
        self.name = name
        self.game_key = game_key
        self.objectives_complete = []
        self.sid = sid
        self.score = 0

        # Tuple: (lat, long)
        self.location = None

        Player.__player_map[self.id] = self
        Player.__player_map[self.sid] = self

    def update_location(self, location):
        self.location = location

    def complete_objective(self, objective_id):
        self.objectives_complete.append(objective_id)
