import React from 'react';
import { connect } from 'react-redux';

import { post } from '../http';
import GameForm from '../components/GameForm';
import { createGame, changeState } from '../actions';
import { CREATE_ENPOINT, OBJECTIVE_SETUP_STATE } from '../constants';

class GameFormPage extends React.Component {
    render() {
        return (
            <div className={`gameForm ${this.props.visible ? '' : 'invisible'}`}>
                <GameForm onSubmit={ this.props.onSubmit } />
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        onSubmit: (values) => {
            const { name, description } = values;
            // create game on server
            post(CREATE_ENPOINT, {
                name,
                description,
            }, (responseJson) => {
                // TODO: handle non 200 status
                console.log('JSON received:', responseJson);
                dispatch(createGame({
                    name,
                    description,
                    key: responseJson.game_key
                }))
                dispatch(changeState(OBJECTIVE_SETUP_STATE));
            })
            // update app state
        }
    };
};

export default connect(undefined, mapDispatchToProps)(GameFormPage)
