import uuid

class Objective:
    __objective_map = {}

    @staticmethod
    def get_by_id(objective_id):
        return Objective.__objective_map[objective_id]

    def __init__(self, location, name, description, gameKey):
        self.id = str(uuid.uuid1())
        self.location = location
        self.name = name
        self.description = description
        self.gameKey = gameKey
        self.players_completed = []

        Objective.__objective_map[self.id] = self

    def player_complete(self, player_id):
        self.players_completed.append(player_id)

