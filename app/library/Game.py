import time
import uuid
from random import randint
from bisect import bisect_left

from Player import Player
from Objective import Objective

def binary_search(seq, num):
    lo = 0
    hi = len(seq)
    while lo < hi:
        mid = (lo + hi)//2
        if num >= seq[mid]: hi = mid
        else: lo = mid + 1
    return hi

class Game:
    __game_map = {}

    @staticmethod
    def get_list():
        return Game.__game_map.keys()

    @staticmethod
    def get_by_key(key):
        return Game.__game_map[key]

    @staticmethod
    def get_by_sid(sid):
        return Game.__game_map[sid]

    def __init__(self, ownerid, sid):
        self.timestamp = time.time()

        while True:
            self.key = "".join(chr(randint(0,25)+65) for i in xrange(4))
            if not self.key in Game.get_list():
                break

        self.ownderid = ownerid
        self.sid = sid
        self.players = {}
        self.objectives = {}
        self.scores = []

        self.started = False
        self.start_time = None

        Game.__game_map[self.key] = self
        Game.__game_map[self.sid] = self
        
    def serialize(self):
    	data = []
        for objective in self.objectives.values():
            data.append({
                "id": str(objective.id),
                "name": objective.name,
                "description": objective.description,
                "location": objective.location
            })
        return data

    def add_player(self, name, sid):
        player = Player(name, self.key, sid)
        self.players[player.id] = player
        self.scores.append(0)

    def player_list(self):
        return self.players.values()

    def update_player_score(self, player):
        score = player.score
        self.scores[binary_search(self.scores), score] += 1
        player.score += 1

    def get_player_rank(self, player):
        return len(self.scores) - binary_search(self.scores, player.score)

    def add_objective(self, latitude, longitude, name, description):
        objective = Objective((latitude, longitude), name, description, self.key)
        self.objectives[objective.location] = objective

    def objective_list(self):
        return self.objectives.values()

    def start(self):
        self.start_time = time.time()
        self.started = True 



