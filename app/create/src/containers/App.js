import React from 'react';
import { connect } from 'react-redux';

import GameFormPage from './GameFormPage';
import OnBoard from './OnBoard';
import ObjectiveSetup from './ObjectiveSetup'
import * as constants from '../constants';

const App = ({ state }) => (
    <div className='App'>
        <OnBoard visible={state === constants.ONBOARD_STATE} />
        <GameFormPage visible={state === constants.CREATE_STATE} />
        <ObjectiveSetup visible = {state === constants.OBJECTIVE_SETUP_STATE} />
    </div>
)

const mapStateToProps = (state) => {
    return {
        state: state.gameInfo.appState,
    }
}

export default connect(mapStateToProps)(App);
