import { connect } from 'react-redux'

import GameForm from '../components/GameForm'
import { createGame } from '../actions'

const mapDispatchToProps = {
  onSubmit: createGame
}

const GameFormPage = connect(()=>{ return {} }, mapDispatchToProps)(GameForm)

export default GameFormPage
