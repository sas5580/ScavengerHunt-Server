import React from 'react';
import { connect } from 'react-redux';

import GameForm from '../components/GameForm';
import { createGame } from '../actions';
import { CREATE_ENPOINT } from '../constants';

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
            fetch(CREATE_ENPOINT, {
                method: 'POST',
                body: JSON.stringify({
                    name,
                    description,
                })
            })
            .then((response) => response.json())
            .then((responseJson) => {
                // TODO: handle non 200 status
                console.log(responseJson);
                dispatch(createGame({
                    name,
                    description,
                    key: responseJson.game_key
                }))
            })
            .catch((error) => {
                console.error(error);
            })
        }
    };
};

export default connect(undefined, mapDispatchToProps)(GameFormPage)
