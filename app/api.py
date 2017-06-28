from flask import jsonify
from app import app, Game


@app.route('/api/game_data/<string:game_id>')
def game_data(game_id):
    if game_id in Game.get_list():
        return jsonify({
            'data': Game.get_by_key(game_id).serialize(),
            'status': 200
        })

    else:
        return jsonify({
            'status': 400,
            'message': 'Invalid game id!'
        })
