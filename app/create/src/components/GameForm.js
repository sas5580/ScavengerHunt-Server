import React from 'react'
import { Field, reduxForm } from 'redux-form'
import PropTypes from 'prop-types'

let GameForm = ({ handleSubmit }) => {
  return (
    <form onSubmit={ handleSubmit }>
      <div>
        <label htmlFor="gameName">Name </label>
        <Field name="gameName" component="input" type="text" />
      </div>
      <div>
        <label htmlFor="gameDescription">Description</label>
        <Field name="gameDescription" component="textarea" type="text" />
      </div>
      <button type="submit">Create!</button>
    </form>
  )
}

GameForm.PropTypes = {
    onSubmit: PropTypes.func.isRequired
}

export default reduxForm({
    form: 'contact'
})(GameForm)

