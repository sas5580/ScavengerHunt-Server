from flask import request, jsonify
from app import app, socketio, Game, Objective, Player

@app.route('/api/game_data/<string:game_id>')
def game_data(game_id):
    if game_id in Game.get_list():
        return jsonify({'data': Game.get_by_key(game_id).serialize()})
    else:
        return "Invalid game id!"

