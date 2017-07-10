const gameInfo = (state = {}, action) => {
  switch (action.type) {
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
