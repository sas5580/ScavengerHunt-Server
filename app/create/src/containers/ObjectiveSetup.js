import React from 'react';
import { connect } from 'react-redux';
import MapLayout from '../components/MapLayout';
import './ObjectiveSetup.css';

const ObjectiveSetup = ({gameName, gameKey, visible}) => {
	return (
		<div className={visible ? '' : 'invisible'}>
			<div className='instruction'>
				Add objectives to '{gameName}'!
			</div>

			<div className='objectiveSetup'>
				<MapLayout />
			</div>
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