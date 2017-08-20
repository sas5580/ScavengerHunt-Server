import React from 'react';
import { connect } from 'react-redux';
import GameFormPage from './GameFormPage';
import OnBoard from './OnBoard';
import ObjectiveSetup from './ObjectiveSetup'
import * as constants from '../constants';

const App = ({ state }) => (
    <div className='App'>
        {state === constants.ONBOARD_STATE && <OnBoard />}
        {state === constants.CREATE_STATE && <GameFormPage />}
        {state === constants.OBJECTIVE_SETUP_STATE && <ObjectiveSetup />}
    </div>
)

const mapStateToProps = (state) => {
    return {
        state: state.gameInfo.appState,
    }
}

export default connect(mapStateToProps)(App);
