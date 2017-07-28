export const changeState = (state) => ({
    type: 'CHANGE_STATE',
    state,
});

export const createGame = (gameInfo) => ({
  type: 'CREATE_GAME',
  gameInfo,
});
