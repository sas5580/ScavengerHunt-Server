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

"""
@app.route('/api/player_rank/', methods=['GET'])
def game_info():
    player_id = request.args.get('player_id')
    game_id = request.args.get('game_id')
    if game_id in Game.get_list():
        if player_id in Game.players:
            print player.name, "requested its rank."
            return jsonify({
                'data': {
                    'rank': rank,
                    'num players': len(game.player_list())
                }
                'status': 200
            })

    return jsonify({
        'status': 400,
        'message': 'Invalid game id!'
    })
"""

##### Game creation endpoints #####

@app.route('/api/create_game/', methods=['POST'])
def create_game():
    print 'Creating game:'

    try: 
        data = json.loads(request.data)
        print data
        name = data['name']
        description = data['description'] if 'description' in data else ''

        game = Game(name, description)

        return jsonify({
            'status': 200,
            'game_key': game.key
        })
    except:
        return jsonify({
            'status': 400,
            'message': 'Invalid payload, can\'t create game'
        })

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
    "objective_id": <String>
}
"""
@app.route('/api/delete_objective/', methods=['POST'])
def delete_objective():
    data = json.loads(request.data)
    game_id = data['game_id']
    if game_id in Game.get_list():
        game = Game.get_by_key(game_id)

        if game.started:
            return jsonify({
                'status': 400,
                'message': 'Can\'t delete objectives if game is in progress'
            })

        game.delete_objective(data['objective_id'])

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


