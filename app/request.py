import datetime
import json
from flask import request
from flask_socketio import emit
from app import app, socketio, Game, Objective, Player

# Fake data
game1 = Game(123, '')
print game1.key

game1.add_player('Yan', '')
game1.add_player('Sas', '')

game1.add_objective(1111, 2222, "name1", "description")
game1.add_objective(3333, 4444, "name2", "description2")

@socketio.on('connect')
def connect():
	print "Someone connected!"

@socketio.on('connection')
def connection(message):
	print "Connection: ", message['data']

	if message['data']['type'] == 'player':
		name = message['data']['name']
		# Use actual game code when implemented
		# game = Game.get_by_key(message['data']['game key'])
		player = game1.add_player(name, request.sid)

		# DEBUG
		print "Current players: "
		for p in game1.player_list():
			print p.name,
		print

	emit('connection', {'data': {'id': str(player.id)}})

@socketio.on('disconnect')
def disconnect():
	player = Player.get_by_id(request.sid)
	print player.name, "disconnected."

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
	objective = Objective.get_by_id(message['data']['objective id'])

	game.player_complete_objective(player, objective)


