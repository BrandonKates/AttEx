import React from 'react';
import { withRouter } from "react-router-dom";

import GrammarContainer from '../components/GrammarContainer';
import ClickableImages from '../components/ClickableImages';

import {RECOGNITION_API, getAPI, postAPI} from '../api';

class GrammarTask extends React.Component {
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
		console.log(this.state)
	}
	getData(){
		return {
			images: this.state.data.images,
		}
	}
	onClick(){
		var data = this.getData();
		this.postAPI(data);
		this.props.history.push('/');
	}

	render(){
		if(this.state.data){
			var { grammar } = this.state.data;
		}

		return (
			<React.Fragment> 
	        	<ClickableImages images={this.props.images} clickable={false}/>
        		<GrammarContainer grammar={grammar} options={this.props.options}/>
	        </React.Fragment> 
		)
	}
}

export default withRouter(GrammarTask);