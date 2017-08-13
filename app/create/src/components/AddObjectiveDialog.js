import React, { Component} from 'react';
import './AddObjectiveDialog.css';

class AddObjectiveDialog extends Component {

	constructor(props){
		super(props);
		this.state={

		}
	}

	render(){
		console.log("add objective");
		return(
			<div className='AddObjectiveDialog'>
				<h2>Add an objective!</h2>

				Selected Lat: {this.props.lat} <br></br>

				Selected Lng: {this.props.lng} <br></br>
			</div>
		)
	}
}

export default AddObjectiveDialog;