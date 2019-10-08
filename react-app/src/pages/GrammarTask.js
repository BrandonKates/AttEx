import React from 'react';
import { withRouter } from "react-router-dom";

import GrammarContainer from '../components/GrammarContainer';
import Canvas from '../components/Canvas';

import {GRAMMAR_API, getAPI, postAPI} from '../api';

class GrammarTask extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			data: null,
			point1: {x: null, y: null},
			point2: {x: null, y: null},
		};
		this.onClick = this.onClick.bind(this);
		this.handleChange1 = this.handleChange1.bind(this);
		this.handleChange2 = this.handleChange2.bind(this);
		this.getAPI = () => getAPI(GRAMMAR_API);
		this.postAPI = (data) => postAPI(GRAMMAR_API, data);
	}
	componentDidMount(){
		this.getAPI().then(data => this.setState({ data: data }));
		//console.log(this.state)
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

	handleChange1(point){
		this.setState({point1: point})
	}

	handleChange2(point){
		this.setState({point2: point})
	}

	render(){
		if(this.state.data){
			var { grammar } = this.state.data;
		}

		return (
			<React.Fragment> 
				<div id="twoCanvas">
					<Canvas image={this.props.images[0]} onChange={this.handleChange1}/>
					<Canvas image={this.props.images[1]} onChange={this.handleChange2}/>	

				</div>	
					Point 1: {this.state.point1.x} {this.state.point1.y} <b/> <b/>
					Point 2: {this.state.point2.x} {this.state.point2.y} <b/> <b/>
					{grammar && <GrammarContainer grammar={grammar} options={this.props.options}/>}
        		{grammar}
	        </React.Fragment> 
		)
	}
}

export default withRouter(GrammarTask);