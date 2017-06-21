from flask import jsonify, make_response
from flask_socketio import emit
from app import app, socketio, Game, Objective, Player
import datetime
import json

@socketio.on('test')
def test_connect():
    print "TEST"
    socketio.emit('my_response', {'data': 'TEST'})

game = Game(123)

game.add_player('Yan')
game.add_player('Sas')

game.add_objective(1111, 2222, "description")
game.add_objective(3333, 4444, "description2")

@socketio.on('my_event')
def test_connect(message):
	print message['data']
	emit('penis', {'data': 'dur'})

@socketio.on('connect')
def connect():
	print "connect"

@socketio.on('disconnect')
def disconnect():
	print "disconnect"

@socketio.on('heart_beat')
def heartBeat(message):
	time = datetime.datetime.now()
	emit('heartbeat',{'data': time})

@socketio.on('get_game_info')
def getGameInfo(message):
	print 'get_game_info: ', message
	
	print message['game']
	
	emit('game_info' , {'data' : 'get game info'})
