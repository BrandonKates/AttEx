import React from 'react';
import { withRouter } from "react-router-dom";

import Button from 'react-bootstrap/Button';

import ClickableImages from '../components/ClickableImages';


import {CHOOSE_API, getAPI, postAPI} from '../api';

class ChooseImageTask extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			data: null,
			selected: null,
		}
		this.onClick = this.onClick.bind(this);
		this.handleChange = this.handleChange.bind(this);
		this.getAPI = () => getAPI(CHOOSE_API);
		this.postAPI = (data) => postAPI(CHOOSE_API, data);
	}
	componentDidMount(){
		this.getAPI().then(data => this.setState({ data: data }));
	}
	getData(){
		return {
			images: this.state.data.images,
			adverb: this.state.data.adverb,
			adjective: this.state.data.adjective,
		}
	}	
	onClick(){
		const selected = this.state.selected;
		if(selected === null){
			window.alert('Please select one of the images.')
			return;
		}
		var data = this.getData();
		data.choice = selected;
		console.log("Choose OnClick Data: ", data);
		this.postAPI(data);
		this.props.history.push('/');
	}
	handleChange(selected){
		this.setState({selected: selected})
	}
	render(){
		if(this.state.data)
			var { adverb, adjective } = this.state.data;
		
		return (     
			<React.Fragment> 
		    	<ClickableImages images={this.props.images} clickable={true} onChange={this.handleChange}/>
		    	<div id='grammar-container'>
	        		<div className='inner-grammar'>
						Click the image that is {adverb} {adjective}.
							<Button variant="primary" type='submit' id='choose-submit' onClick={() => this.onClick()}>Submit</Button> 
					</div>
	        	</div>
		  	</React.Fragment>
		)
	}
}

export default withRouter(ChooseImageTask);