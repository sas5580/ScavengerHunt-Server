from flask import request
from flask_socketio import emit
from app import app, socketio, Game, Objective, Player
import datetime
import json

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
	player = 

@socketio.on('heart_beat')
def heartBeat(message):
	time = datetime.datetime.now()
	emit('heartbeat', {'data': time})

@socketio.on('get_game_info')
def getGameInfo(message):
	print 'get_game_info: ', message
	
	print message['game']
	
	emit('game_info' , {'data' : 'get game info'})

@socketio.on('my_event')
def test_connect(message):
	print message['data']
	emit('penis', {'data': 'dur'})
