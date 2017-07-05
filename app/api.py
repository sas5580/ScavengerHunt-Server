from flask import jsonify, request
from app import app, Game, Player, Objective
import json


@app.route('/api/game_info/', methods=['GET'])
def game_info():
    game_id = request.args.get('game_id')
    if game_id in Game.get_list():
        return jsonify({
            'data': Game.get_by_key(game_id).serialize_objectives(),
            'status': 200
        })

    return jsonify({
        'status': 400,
        'message': 'Invalid game id!'
    })

##### Game creation endpoints #####

# Expects data to look like:
"""
{
    "game_id": <string>
    "objective": {
        "name": <string>
        "description": <string>
        "location": {
            "lat": <Number>
            "long": <Number>
        }
    }
}
"""
@app.route('/api/add_objective/', methods=['POST'])
def add_objective():
    data = json.loads(request.data)
    game_id = data['game_id']
    if game_id in Game.get_list():
        game = Game.get_by_key(game_id)

        if not 'objective' in data:
            return jsonify({
                'status': 400,
                'message': 'Missing objective data'
            })

        name = data['objective']['name']
        description = data['objective']['description']
        location = data['objective']['location']
        objective = game.add_objective(location, name, description)

        return jsonify({
            'status': 200
        })

    return jsonify({
        'status': 400,
        'message': 'Invalid game id!'
    })

# Expects data to look like:
"""
{
    "game_id": <String>
}
"""

@app.route('/api/game_stats/', methods=['POST'])
def game_stats():
    data = json.loads(request.data)
    game_id = data['game_id']
    if game_id in Game.get_list():
        game = Game.get_by_key(game_id)

        objective_stats = []
        for objective in game.objective_list():
            players_complete = [{
                'id': player_id,
                'name': Player.get_by_id(player_id).name
            } for player_id in objective.players_completed]

            objective_stats.append({
                'id': objective.id,
                'players_complete': players_complete
            })

        player_stats = []
        for player in game.player_list():
            player_info = player.serialize()
            player_info['rank'] = game.get_player_rank(player)
            player_stats.append(player_info)

        return jsonify({
            'data': {
                'objective_stats': objective_stats,
                'player_stats': player_stats
            },
            'status': 200
        })

    return jsonify({
        'status': 400,
        'message': 'Invalid game id!'
    })


