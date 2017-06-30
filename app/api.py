from flask import jsonify, request
from app import app, Game, Player, Objective


@app.route('/api/game_info/', methods=['GET'])
def game_info():
    game_id = request.args.get('game_id')
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


@app.route('/api/game_stats/', methods=['GET'])
def game_stats():
    game_id = request.args.get('game_id')
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

    else:
        return jsonify({
            'status': 400,
            'message': 'Invalid game id!'
        })
