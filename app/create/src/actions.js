import { CREATE_ENPOINT } from './constants';

export const changeState = (state) => ({
    type: 'CHANGE_STATE',
    state,
});

export const createGame = (gameInfo) => {
    const { name, description } = gameInfo;
    return {
        type: 'CREATE_GAME',
        gameInfo,
    }
}

