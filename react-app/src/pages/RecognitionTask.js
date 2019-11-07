import React from 'react';
import { withRouter } from "react-router-dom";

import {Form, Button} from 'react-bootstrap';

import ClickableImages from '../components/ClickableImages';
import Creatable from 'react-select/creatable'

import {RECOGNITION_API, getAPI, postAPI} from '../api';

class RecognitionTask extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			data: null,
		};
		this.onClick = this.onClick.bind(this);
		this.getAPI = () => getAPI(RECOGNITION_API);
		this.postAPI = (data) => postAPI(RECOGNITION_API, data);
	}
	componentDidMount(){
		this.getAPI().then(data => this.setState({ data: data }));
	}
	getData(){
		return {
			images: this.state.data.images,
			classLabel: this.state.data.classLabel,
		}
	}
	onClick(bool){
		var data = this.getData();
		data.choice = bool;
		this.postAPI(data);
		this.props.history.push('/');
	}

	render(){
		if(this.state.data){
			console.log("Recognition: ", this.state.data)
			var { images, classLabel } = this.state.data;
		}

		return (
			<div>
			<React.Fragment> 
	        	{images && <ClickableImages images={images} clickable={false}/> }
	        	<div id='grammar-container'>
	        		<div className='inner-grammar'>
						What is this?  Choose from existing classes or enter new one					
					</div>
					
	        	</div>
	
			</React.Fragment> 
			<div>
			<Creatable
						isClearable
						options = {[{label:"Goose", value : "goose"}, {label:"Cat", value : "cat"}]}></Creatable>
			<Button>Submit</Button>
			</div>
			</div>
		)
	}
}

export default withRouter(RecognitionTask);


/*
API:
get: maps data into data
  - data.images
  - data.objectClass

post: send data from
  - data.images
  - data.objectClass
  - data.choice //did we accept or reject the randomnly guessed label?

*/