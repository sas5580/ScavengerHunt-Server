import datetime
import json
from flask import request
from flask_socketio import emit
from app import app, socketio, Game, Objective, Player

# Fake data
game = Game(123, '')
print game.key
print len(Game.get_list())

game.add_player('Yan', '')
game.add_player('Sas', '')

game.add_objective(1111, 2222, "name1", "description")
game.add_objective(3333, 4444, "name2", "description2")

@socketio.on('connect')
def connect():
	print "Someone connected!"

@socketio.on('connection')
def connection(message):
	print "Connection: ", message['data']

	if message['data']['type'] == 'player':
		name = message['data']['name']
		game.add_player(name, request.sid)

		# DEBUG
		print "Current players: "
		for p in game.player_list():
			print p.name,
		print

@socketio.on('disconnect')
def disconnect():
	print "disconnect"

@socketio.on('rank')
def rank():
	player = Player.get_by_id(request.sid)
	print player.name, "requested its rank."

	game = Game.get_by_key(player.game_key)
	rank = game.get_player_rank(player)

	emit('rank', {'data': {'rank': rank}})
