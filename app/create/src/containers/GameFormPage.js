import React from 'react';
import { connect } from 'react-redux'

import GameForm from '../components/GameForm'
import { createGame } from '../actions'

class GameFormPage extends React.Component {
    render() {
        return (
            <div className={`gameForm ${this.props.visible ? '' : 'invisible'}`}>
                <GameForm handleSubmit={this.props.onSubmit} />
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => {
  onSubmit: () => {dispatch(createGame());}
};

export default connect(undefined, mapDispatchToProps)(GameFormPage)
