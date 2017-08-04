import React from 'react';
import { connect } from 'react-redux'

import GameForm from '../components/GameForm'
import { createGame } from '../actions'

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
            dispatch(createGame(values));
        }
    };
};

export default connect(undefined, mapDispatchToProps)(GameFormPage)
