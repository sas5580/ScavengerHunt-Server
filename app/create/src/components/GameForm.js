import React from 'react'
import { Field, reduxForm } from 'redux-form'
import PropTypes from 'prop-types'

const GameForm = ({ handleSubmit }) => {
    return (
    <form onSubmit={ handleSubmit }>
        <div>
            <label htmlFor="name">Name </label>
            <Field name="name" component="input" type="text" />
        </div>
        <div>
            <label htmlFor="description">Description</label>
            <Field name="description" component="textarea" type="text" />
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

