import datetime
import json
from flask import request
from flask_socketio import emit
from app import app, socketio, Game, Objective, Player

# Fake data
game1 = Game('game1')
print game1.key

game1.add_player('Yan', '')
game1.add_player('Sas', '')

game1.add_objective({"lat": 1111, "long": 2222}, "name1", "description")
game1.add_objective({"lat": 3333, "long": 4444}, "name2", "description2")

for o in game1.objective_list():
    print o.id


@socketio.on('connect')
def connect():
    print "Someone connected!"


@socketio.on('connection')
def connection(message):
    print "Connection: ", message['data']

    if message['data']['type'] == 'player':
        if 'playerId' in message['data']:
            player = Player.get_by_id(message['data']['playerId'])
            if player.active:
                return

            player.update_sid(request.sid)
            emit('connection', {'data': {'objectives complete': player.objectives_complete}})

        else:
            name = message['data']['name']
            # Use actual game code when implemented
            # game = Game.get_by_key(message['data']['game key'])
            player = game1.add_player(name, request.sid)

        emit('connection', {'data': {'id': player.id}})

        # DEBUG
        print "Current players: "
        for p in game1.player_list():
            print p.name,
        print

@socketio.on('disconnect')
def disconnect():
    player = Player.get_by_id(request.sid)
    if player:
        print player.name, "disconnected."
        game = Game.get_by_key(player.game_key)
        game.deactivate_player(player)
    else:
        print "Someone disconnected"


@socketio.on('rank')
def rank():
    player = Player.get_by_id(request.sid)
    print player.name, "requested its rank."

    game = Game.get_by_key(player.game_key)
    rank = game.get_player_rank(player)

    emit('rank', {'data': {'rank': rank}})


@socketio.on('objective')
def rank(message):
    player = Player.get_by_id(request.sid)
    print player.name, "completed an objective."

    game = Game.get_by_key(player.game_key)
    objective = Objective.get_by_id(message['data']['objectiveId'])

    game.player_complete_objective(player, objective)
