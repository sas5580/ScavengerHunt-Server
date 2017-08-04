import { CREATE_ENPOINT } from './constants';

export const changeState = (state) => ({
    type: 'CHANGE_STATE',
    state,
});

export const createGame = (gameInfo) => {
    const { name, description } = gameInfo;
    fetch(CREATE_ENPOINT, {
        headers: {
            'Access-Control-Allow-Origin': '*'
        },
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({
            name,
            description,
        })
    })
    .then((response) => response.json())
    .then((responseJson) => {
        // TODO: handle non 200 status
        return {
            type: 'CREATE_GAME',
            name,
            description,
            key: responseJson.game_key
        }
    })
    .catch((error) => {
        console.error(error);
    });

    return {
        type: 'CREATE_GAME',
        gameInfo,
    }
}

