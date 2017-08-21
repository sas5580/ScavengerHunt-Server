import React from 'react';
import { connect } from 'react-redux';
import MapLayout from '../components/MapLayout';
import './ObjectiveSetup.css';

const ObjectiveSetup = ({ gameName, gameKey }) => {
	return (
		<div className='objectiveSetup'>
			<div className='instruction'>
				Add objectives to '{gameName}'!
			</div>
			<MapLayout gameKey={gameKey}/>
		</div>
	);
}


const mapStateToProps = (state) => {
    return {
        gameName: state.gameInfo.name,
        gameKey: state.gameInfo.key,
    }
}

export default connect(mapStateToProps)(ObjectiveSetup);