import React from 'react';
import { withRouter } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import SelectForm from '../components/SelectForm'
import GrammarContainer from '../components/GrammarContainer';
import Canvas from '../components/Canvas';

import { GRAMMAR_API, getAPI, postAPI } from '../api';

class GrammarTask extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			data: null,
			point1: { x: null, y: null },
			point2: { x: null, y: null },
		};
		this.onClick = this.onClick.bind(this);
		this.handleChange1 = this.handleChange1.bind(this);
		this.handleChange2 = this.handleChange2.bind(this);
		this.getAPI = () => getAPI(GRAMMAR_API);
		this.postAPI = (data) => postAPI(GRAMMAR_API, data);
	}
	componentDidMount() {
		this.getAPI().then(data => this.setState({ data: data }));
		//console.log(this.state)
	}
	getData() {
		return {
			images: this.state.data.images,
		}
	}
	onClick() {
		var data = this.getData();
		this.postAPI(data);
		this.props.history.push('/');
	}


	handleChange1(point) {
		this.setState({ point1: point })
	}

	handleChange2(point) {
		this.setState({ point2: point })
	}

	render() {
		if (this.state.data) {
			var { grammar, images } = this.state.data;
			console.log(images)
		}

		return (
			<React.Fragment>
				{images && <div id="twoCanvas">
					<Canvas image={images[0]} onChange={this.handleChange1} />
					<Canvas image={images[1]} onChange={this.handleChange2} />

				</div>}
				
				{grammar && <GrammarContainer grammar={grammar} options={this.props.options} />}
				
			</React.Fragment>
			
		)
	}
}

export default withRouter(GrammarTask);