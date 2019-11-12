import React from 'react';
import { withRouter } from "react-router-dom";

import Button from 'react-bootstrap/Button';

import ClickableImages from '../components/ClickableImages';

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
			<React.Fragment> 
	        	{images && <ClickableImages images={images} clickable={false}/> }
	        	<div id='grammar-container'>
	        		<div className='inner-grammar'>
						What do you see in this image? {classLabel}
							<Button variant="secondary" type='submit' id='recognition-yes' onClick={() => this.onClick(true)}>Yes</Button> 
							<Button variant="secondary" type='submit' id='recognition-no' onClick={() => this.onClick(false)}>No</Button>
					</div>
	        	</div>
	        </React.Fragment> 
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