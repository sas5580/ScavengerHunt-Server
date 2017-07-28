import React from 'react';
import { connect } from 'react-redux';
import { changeState } from '../actions';
import { CREATE_STATE } from '../constants';

import './OnBoard.css';
import logo from '../logo.png'

const OnBoard = ({ visible, onCreateClick }) => {
    return (
        <div className={`onBoard ${visible ? '' : 'invisible'}`}>
            <div className='logo'>
                <img src={logo} />
            </div>
            <button className='button -regular -green' id='createBtn' onClick={onCreateClick}>
                Create
            </button>
            <button className='button -regular -blue    ' id='trackBtn'>
                Track
            </button>
        </div>
    );
}

const mapDispatchToProps = (dispatch) => {
    return {
        onCreateClick: () => {
            dispatch(changeState(CREATE_STATE));
        }
    }
}


export default connect(undefined, mapDispatchToProps)(OnBoard);
