import * as constants from '../constants';

const initialState = {
    appState: constants.ONBOARD_STATE,
}

const gameInfo = (state = initialState, action) => {
  switch (action.type) {
    case 'CHANGE_STATE':
      return {
        ...state,
        appState: action.state,
      }
    case 'CREATE_GAME':
      return {
        ...state,
        ...action.gameInfo
      }
    default:
      return state
  }
}

export default gameInfo
