import React from 'react';
import { withRouter } from "react-router-dom";

import Button from 'react-bootstrap/Button';

import Canvas from '../components/Canvas';

import {CLICK_API, getAPI, postAPI} from '../api';

class ClickPointTask extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			data: null,
			point: {x: null, y: null}
		}
		this.onClick = this.onClick.bind(this);
		this.handleChange = this.handleChange.bind(this);
		this.getAPI = () => getAPI(CLICK_API);
		this.postAPI = (data) => postAPI(CLICK_API, data);
	}
	componentDidMount(){
		this.getAPI().then(data => this.setState({ data: data }));
	}
	getData(){
		return {
			images: this.state.data.images,
			attribute: this.state.data.attribute,
			point: this.state.point,
		}
	}	
	onClick(bool){

		var data = this.getData();
		data.choice = bool;		
		console.log("Choose OnClick Data: ", data);
		this.postAPI(data);
		this.props.history.push('/');
	}
	handleChange(point){
		this.setState({point: point})
	}
	render(){
		if(this.state.data){
			var { attribute, images } = this.state.data;
			console.log(images)
		}

		return (     
			<React.Fragment> 
		    	{images && <Canvas image={images[0]} onChange={this.handleChange}/>}
		    	<div id='grammar-container'>
	        		<div className='inner-grammar'>
						Click the point where {attribute} is located in the image. Does the image contain {attribute}?
							<Button variant="secondary" type='submit' id='choose-yes' onClick={() => this.onClick(true)}>Yes</Button> 
							<Button variant="secondary" type='submit' id='choose-no' onClick={() => this.onClick(false)}>No</Button>
					</div>
	        	</div>
		  	</React.Fragment>
		)
	}
}

export default withRouter(ClickPointTask);